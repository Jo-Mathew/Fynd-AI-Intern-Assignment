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

DATA_FILE = "feedback_data.csv"

def load_data():
    if not os.path.exists(DATA_FILE):
        return pd.DataFrame()

    df = pd.read_csv(DATA_FILE)

    df["ai_summary"] = df["ai_summary"].fillna("").astype(str)
    df["recommended_action"] = df["recommended_action"].fillna("").astype(str)

    return df


def generate_summary_and_action(review, rating):
    prompt = f"""
You are an AI assistant for business owners.

User Rating: {rating}
User Review: "{review}"

Generate:
1. A concise summary of the feedback
2. A recommended action for the business owner
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    lines = response.text.strip().split("\n")
    summary = lines[0]
    action = lines[-1]

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
        df.to_csv(DATA_FILE, index=False)

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
