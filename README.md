# Fynd-AI-Intern-Assignment 1 & 2

Required Dashboard Links:
<ul>
    <li><strong>User Dashboard:</strong> Users can select a star rating, write a review, submit it, and receive an AI-generated response. 
        <br>Access it here: <a href="https://huggingface.co/spaces/Jo-Mathew/user-reviews-dashboard" target="_blank">User Dashboard Link</a>
    </li>
    <li><strong>Admin Dashboard:</strong> Admins can view all submissions live, including user ratings, reviews, AI-generated summaries, and recommended actions. Analytics are also provided. 
        <br>Access it here: <a href="https://huggingface.co/spaces/Jo-Mathew/admin-feedback-dashboard" target="_blank">Admin Dashboard Link</a>
    </li>
</ul>

<h1>Task 1: Yelp Review Rating Prediction</h1>

<h2>Overview</h2>
<p>This project predicts Yelp review ratings (1–5 stars) using large language model prompting. Three prompting strategies were designed and evaluated on a sample of 100 reviews.</p>

<h2>Model Used</h2>
<p>The task uses the <strong>Gemini 2.5 Flash</strong> model from Google GenAI for predicting Yelp review ratings via prompting. 
This is the free-tier version of the model.</p>

<h2>Prompting Approach</h2>
<ul>
    <li><strong>Direct Prompt:</strong> The model predicts ratings directly from reviews with JSON output.</li>
    <li><strong>Few-Shot Prompt:</strong> Example reviews with ratings are provided before predicting new reviews.</li>
    <li><strong>Guided Prompt:</strong> The model first assesses sentiment, maps it to a star rating, and provides a brief explanation.</li>
</ul>
<img width="1122" height="483" alt="image" src="https://github.com/user-attachments/assets/b7876e13-aefb-4b78-9a8a-6a627be23355" />

<h2>Evaluation Results</h2>
<p>Accuracy and JSON validity for each prompting approach:</p>
<table border="1" cellpadding="5">
    <tr><th>Prompt</th><th>Accuracy</th><th>JSON Validity</th></tr>
    <tr><td>Direct</td><td>0.65</td><td>1.0</td></tr>
    <tr><td>Few-Shot</td><td>0.67</td><td>1.0</td></tr>
    <tr><td>Guided</td><td>0.66</td><td>1.0</td></tr>
</table>

<h2>Setup Instructions</h2>
<ol>
    <li>Create a <code>.env</code> file with your API key:
        <pre>GEMINI_API_KEY=your_key_here</pre>
    </li>
    <li>Install dependencies:
        <pre>pip install pandas python-dotenv google-genai</pre>
    </li>
    <li>Run the notebook: <code>Task_1_Python_Notebook.ipynb</code></li>
</ol>

<h2>Notes</h2>
<ul>
    <li>Used 100 reviews due to free-tier API limits.</li>
    <li>Predictions and evaluation results are saved to CSV.</li>
    <li>The three prompting strategies were designed to improve guidance, JSON validity, and prediction accuracy.</li>
</ul>

<h1>Task 2: Two-Dashboard AI Feedback System</h1>

<h2>Overview</h2>
<p>This project implements a web-based AI feedback system with two dashboards: a public-facing User Dashboard and an internal Admin Dashboard. 
Users can submit ratings and reviews, and AI generates responses. The Admin Dashboard provides summaries, recommended actions, and analytics.</p>

<h2>Dashboards</h2>
<ul>
    <li><strong>User Dashboard:</strong> Users can select a star rating, write a review, submit it, and receive an AI-generated response. 
        <br>Access it here: <a href="https://huggingface.co/spaces/Jo-Mathew/user-reviews-dashboard" target="_blank">User Dashboard Link</a>
    </li>
    <li><strong>Admin Dashboard:</strong> Admins can view all submissions live, including user ratings, reviews, AI-generated summaries, and recommended actions. Analytics are also provided. 
        <br>Access it here: <a href="https://huggingface.co/spaces/Jo-Mathew/admin-feedback-dashboard" target="_blank">Admin Dashboard Link</a>
    </li>
</ul>

<h2>Model Used</h2>
<p>The system uses <strong>Gemini 2.5 Flash</strong> from Google GenAI to:</p>
<ul>
    <li>Generate AI responses for users</li>
    <li>Summarize user feedback</li>
    <li>Suggest recommended actions for business owners</li>
</ul>


<h2>Data Storage</h2>
<p>All feedback is stored in a shared Google Sheet that both dashboards read and write to. This ensures real-time synchronization between User and Admin dashboards.</p>


<h2>Setup Instructions</h2>
<ol>
    <li>Clone the repository.</li>
    <li>Create a <code>.env</code> file with your GenAI API key and Google service account JSON:
        <pre>
GEMINI_API_KEY=your_key_here
GOOGLE_CREDS_JSON='{"type": "service_account", ... }'
        </pre>
    </li>
    <li>Install dependencies:
        <pre>pip install streamlit pandas google-genai gspread oauth2client python-dotenv</pre>
    </li>
    <li>Run the User Dashboard:
        <pre>streamlit run app_user.py</pre>
    </li>
    <li>Run the Admin Dashboard:
        <pre>streamlit run app_admin.py</pre>
    </li>
</ol>

