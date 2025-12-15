# Fynd-AI-Intern-Assignment

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Task 1 - Yelp Review Rating Prediction</title>
    <style>
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>Task 1: Yelp Review Rating Prediction</h1>

    <h2>Overview</h2>
    <p>Predict Yelp review ratings (1–5 stars) using LLM prompting. Three prompt types were implemented and evaluated on 100 sampled reviews.</p>

    <h2>Prompt Types</h2>

    <h3>1. Direct Prompt</h3>
    <pre><code>
You are a Yelp review rating classifier.
Predict a star rating (1–5) for each review.
Output only valid JSON:
[
  {"predicted_stars":4,"explanation":"Brief reasoning"}
]
Reviews:
1. "Sample review..."
2. "Sample review..."
    </code></pre>

    <h3>2. Few-Shot Prompt</h3>
    <pre><code>
You are a Yelp review rating classifier.
Examples:
Review: "Terrible service."
Output: {"predicted_stars":1,"explanation":"Negative experience."}
Review: "Amazing food."
Output: {"predicted_stars":5,"explanation":"Very positive."}
Now classify the following reviews:
[
  {"predicted_stars":4,"explanation":"Brief reasoning"}
]
Reviews:
1. "Sample review..."
2. "Sample review..."
    </code></pre>

    <h3>3. Guided Prompt</h3>
    <pre><code>
You are a Yelp review rating classifier.
1. Assess sentiment (negative/mixed/positive)
2. Map sentiment to 1–5 stars
3. Provide brief explanation
Output JSON only:
[
  {"predicted_stars":3,"explanation":"Mixed sentiment"}
]
Reviews:
1. "Sample review..."
2. "Sample review..."
    </code></pre>

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
    </ul>
</body>
</html>
