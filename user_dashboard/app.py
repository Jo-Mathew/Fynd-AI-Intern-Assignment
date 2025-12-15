import streamlit as st
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv
from google import genai

client = genai.Client()

DATA_FILE = "feedback_data.csv"

def init_storage():
    """Create CSV file if it doesn't exist"""
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=[
            "timestamp",
            "user_rating",
            "user_review",
            "ai_response",
            "ai_summary",
            "recommended_action"
        ])
        df.to_csv(DATA_FILE, index=False)

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
    """Save feedback to CSV"""
    df = pd.read_csv(DATA_FILE)

    new_row = {
        "timestamp": datetime.now().isoformat(),
        "user_rating": rating,
        "user_review": review,
        "ai_response": ai_response,
        "ai_summary": "",
        "recommended_action": ""
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)


# Streamlit UI
# ----------------------------
st.set_page_config(page_title="User Feedback Dashboard", page_icon="⭐")
st.title("⭐ Customer Feedback")

st.write("Please rate your experience and leave a short review.")

init_storage()

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
