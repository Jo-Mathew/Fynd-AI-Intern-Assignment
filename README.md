# Fynd-AI-Intern-Assignment

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Task 1 - Yelp Review Rating Prediction</title>
</head>
<body>
    <h1>Task 1: Yelp Review Rating Prediction</h1>

    <h2>Overview</h2>
    <p>Predict Yelp review ratings (1–5 stars) using LLM prompting. Three prompt types were implemented and evaluated on 100 sampled reviews.</p>

    <h2>Prompting Approach</h2>
    <p>
        Three prompting strategies were used:
        <ul>
            <li><strong>Direct Prompt:</strong> Ask the model to predict the rating for each review directly, with JSON output.</li>
            <li><strong>Few-Shot Prompt:</strong> Provide examples of reviews with ratings before asking the model to classify new reviews.</li>
            <li><strong>Guided Prompt:</strong> Ask the model to assess sentiment first, map it to a star rating, and give a brief explanation.</li>
        </ul>
    </p>

    <h2>Results</h2>
    <table border="1" cellpadding="5">
        <tr><th>Prompt</th><th>Accuracy</th><th>JSON Validity</th></tr>
        <tr><td>Direct</td><td>0.65</td><td>1.0</td></tr>
        <tr><td>Few-Shot</td><td>0.67</td><td>1.0</td></tr>
        <tr><td>Guided</td><td>0.66</td><td>1.0</td></tr>
    </table>

    <h2>Setup</h2>
    <ol>
        <li>Create <code>.env</code> with: <pre>GEMINI_API_KEY=your_key_here</pre></li>
        <li>Install dependencies: <pre>pip install pandas python-dotenv google-genai</pre></li>
        <li>Run <code>Task1_Yelp_Prompting.ipynb</code></li>
    </ol>

    <h2>Notes</h2>
    <ul>
        <li>Sampled 100 reviews due to free-tier API limits.</li>
        <li>Predictions and evaluation results are saved to CSV.</li>
        <li>Prompting approaches were designed to improve model guidance and JSON reliability.</li>
    </ul>
</body>
</html>

