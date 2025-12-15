import streamlit as st
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv
from google import genai

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


def generate_ai_response(rating, review):
    """Generate user-facing AI response"""
    prompt = f"""
You are a polite customer support assistant.

The user gave a rating of {rating} stars and wrote the following review:
"{review}"

Write a short, empathetic response addressing the user's feedback.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()

def save_feedback(rating, review, ai_response):
    sheet.append_row([
        datetime.now().isoformat(),
        rating,
        review,
        ai_response,
        "",   # ai_summary (admin fills)
        ""    # recommended_action (admin fills)
    ])



# Streamlit UI
# ----------------------------
st.set_page_config(page_title="User Feedback Dashboard", page_icon="⭐")
st.title("⭐ Customer Feedback")

st.write("Please rate your experience and leave a short review.")



rating = st.selectbox(
    "Select your rating:",
    options=[1, 2, 3, 4, 5],
    format_func=lambda x: "⭐" * x
)

review = st.text_area(
    "Write your review:",
    placeholder="Share your experience..."
)

submit = st.button("Submit Feedback")

if submit:
    if not review.strip():
        st.warning("Please write a review before submitting.")
    else:
        with st.spinner("Generating AI response..."):
            ai_response = generate_ai_response(rating, review)
            save_feedback(rating, review, ai_response)

        st.success("Thank you for your feedback!")
        st.subheader("AI Response")
        st.write(ai_response)
