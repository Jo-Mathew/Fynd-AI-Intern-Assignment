# Fynd-AI-Intern-Assignment

<h1>Task 1: Yelp Review Rating Prediction</h1>

<h2>Overview</h2>
<p>This project predicts Yelp review ratings (1–5 stars) using large language model prompting. Three prompting strategies were designed and evaluated on a sample of 100 reviews.</p>

<h2>Prompting Approach</h2>
<ul>
    <li><strong>Direct Prompt:</strong> The model predicts ratings directly from reviews with JSON output.</li>
    <li><strong>Few-Shot Prompt:</strong> Example reviews with ratings are provided before predicting new reviews.</li>
    <li><strong>Guided Prompt:</strong> The model first assesses sentiment, maps it to a star rating, and provides a brief explanation.</li>
</ul>

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
    <li>Run the notebook: <code>Task1_Yelp_Prompting.ipynb</code></li>
</ol>

<h2>Notes</h2>
<ul>
    <li>Used 100 reviews due to free-tier API limits.</li>
    <li>Predictions and evaluation results are saved to CSV.</li>
    <li>The three prompting strategies were designed to improve guidance, JSON validity, and prediction accuracy.</li>
</ul>

