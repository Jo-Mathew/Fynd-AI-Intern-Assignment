import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from google import genai

st.set_page_config(
    page_title="Admin Dashboard | AI Feedback System",
    layout="wide"
)

st.title("📊 Admin Dashboard")
st.caption("Monitor user feedback, AI summaries, and recommended actions")

client = genai.Client()


import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load Google credentials from HF Secret
creds_dict = json.loads(os.environ["GOOGLE_CREDS_JSON"])

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
gs_client = gspread.authorize(creds)

sheet = gs_client.open("feedback").sheet1

def load_data():
    records = sheet.get_all_records()
    if not records:
        return pd.DataFrame()

    df = pd.DataFrame(records)

    # Ensure string columns
    df["ai_summary"] = df["ai_summary"].fillna("").astype(str)
    df["recommended_action"] = df["recommended_action"].fillna("").astype(str)

    return df


def generate_summary_and_action(review, rating):
    prompt = f"""
You are an AI assistant for business owners.

User Rating: {rating}
User Review: "{review}"

Return EXACTLY in this format (no extra text):

SUMMARY: <one concise sentence>
ACTION: <one clear recommended action>
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    summary = ""
    action = ""

    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("SUMMARY:"):
            summary = line.replace("SUMMARY:", "").strip()
        elif line.startswith("ACTION:"):
            action = line.replace("ACTION:", "").strip()

    return summary, action


def update_missing_ai_fields(df):
    updated = False

    for idx, row in df.iterrows():
        summary_val = str(row["ai_summary"]).strip().lower()
        action_val = str(row["recommended_action"]).strip().lower()

        if summary_val in ["", "nan"] or action_val in ["", "nan"]:
            summary, action = generate_summary_and_action(
                row["user_review"],
                row["user_rating"]
            )

            df.at[idx, "ai_summary"] = summary
            df.at[idx, "recommended_action"] = action
            updated = True

    if updated:
        # Rewrite entire sheet safely
        sheet.clear()
        sheet.append_row(df.columns.tolist())

        for _, row in df.iterrows():
            sheet.append_row(row.astype(str).tolist())

    return df


df = load_data()


if df.empty:
    st.info("No feedback submissions yet.")
    st.stop()

with st.spinner("Generating AI summaries and recommendations..."):
    df = update_missing_ai_fields(df)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Feedback", len(df))

with col2:
    st.metric("Average Rating", round(df["user_rating"].mean(), 2))

with col3:
    low_ratings = (df["user_rating"] <= 2).sum()
    st.metric("Low Ratings (≤2)", low_ratings)

st.divider()


st.subheader("📈 Analytics")

# Rating distribution bar chart (compact)
rating_counts = df["user_rating"].value_counts().sort_index()

st.bar_chart(
    rating_counts,
    height=300  
)

# Analytics Table

st.subheader("📈 All Feedback Data")

st.dataframe(
    df[[
        "user_rating",
        "user_review",
        "ai_summary",
        "recommended_action"
    ]],
    use_container_width=True
)
