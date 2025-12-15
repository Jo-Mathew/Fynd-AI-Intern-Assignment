# Fynd-AI-Intern-Assignment

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Task 1 - Yelp Review Rating Prediction via Prompting</title>
</head>
<body>
    <h1>Task 1: Yelp Review Rating Prediction via Prompting</h1>

    <h2>Overview</h2>
    <p>This task involves predicting Yelp review ratings (1–5 stars) using prompt engineering with LLMs. We designed multiple prompting approaches and evaluated their performance on a sampled dataset.</p>

    <h2>Dataset</h2>
    <ul>
        <li>Yelp Reviews dataset from Kaggle: <a href="https://www.kaggle.com/datasets/omkarsabnis/yelp-reviewsdataset" target="_blank">Link</a></li>
        <li>Sampled subset (~100 rows) for efficiency and free-tier API limitations</li>
        <li>Columns used: <code>text</code> (review content), <code>stars</code> (actual rating)</li>
    </ul>

    <h2>Prompting Approaches</h2>
    <p>We implemented three prompt types:</p>

    <h3>1. Direct Prompt</h3>
    <pre>
You are a Yelp review rating classifier.
For each review, predict a star rating from 1 to 5.
Rules:
- Output ONLY a valid JSON array
- One JSON object per review
- No extra text or markdown
- predicted_stars must be an integer from 1 to 5
Format:
[
  {"predicted_stars":4,"explanation":"Brief reasoning"}
]
Reviews:
1. "Sample review text..."
2. "Sample review text..."
    </pre>

    <h3>2. Few-Shot Prompt</h3>
    <pre>
You are a Yelp review rating classifier.
Examples:
Review: "Terrible service and cold food."
Output: {"predicted_stars":1,"explanation":"Strongly negative experience."}
Review: "Amazing food and friendly staff."
Output: {"predicted_stars":5,"explanation":"Very positive experience."}
Now classify the following reviews.
Rules:
- Output ONLY a valid JSON array
- One JSON object per review
- No extra text or markdown
- predicted_stars must be an integer from 1 to 5
Format:
[
  {"predicted_stars":4,"explanation":"Brief reasoning"}
]
Reviews:
1. "Sample review text..."
2. "Sample review text..."
    </pre>

    <h3>3. Guided Prompt</h3>
    <pre>
You are a Yelp review rating classifier.
For each review:
1. Assess overall sentiment (negative, mixed, positive)
2. Map sentiment to a 1–5 star rating
3. Provide a brief explanation
Rules:
- Output ONLY a valid JSON array
- One JSON object per review
- No extra text or markdown
- predicted_stars must be an integer from 1 to 5
Format:
[
  {"predicted_stars":3,"explanation":"Mixed sentiment"}
]
Reviews:
1. "Sample review text..."
2. "Sample review text..."
    </pre>

    <h2>Evaluation</h2>
    <p>The evaluation metrics included:</p>
    <ul>
        <li><strong>Accuracy:</strong> Predicted stars vs actual stars</li>
        <li><strong>JSON Validity:</strong> Whether the LLM output was valid JSON</li>
    </ul>

    <h3>Results</h3>
    <table border="1" cellpadding="5" cellspacing="0">
        <tr>
            <th>Prompt Type</th>
            <th>Accuracy</th>
            <th>JSON Validity</th>
        </tr>
        <tr>
            <td>Direct</td>
            <td>0.65</td>
            <td>1.0</td>
        </tr>
        <tr>
            <td>Few-Shot</td>
            <td>0.67</td>
            <td>1.0</td>
        </tr>
        <tr>
            <td>Guided</td>
            <td>0.66</td>
            <td>1.0</td>
        </tr>
    </table>

    <h2>Environment Setup</h2>
    <ol>
        <li>Create a <code>.env</code> file in the notebook folder with the following content:
            <pre>
GEMINI_API_KEY=your_google_gemini_api_key
            </pre>
        </li>
        <li>Install dependencies:
            <pre>pip install pandas python-dotenv google-genai</pre>
        </li>
        <li>Run the notebook: <code>Task1_Yelp_Prompting.ipynb</code></li>
    </ol>

    <h2>Folder Structure</h2>
    <pre>
Task1_Yelp_Prompting/
│
├─ Task1_Yelp_Prompting.ipynb      # Notebook with code
├─ .env                            # GEMINI_API_KEY
├─ requirements.txt                # Python dependencies
└─ README.html                     # This HTML README
    </pre>

    <h2>Usage</h2>
    <p>Open the notebook and run all cells. The notebook will generate predictions for the sampled reviews, evaluate them, and save results to CSV files.</p>

    <h2>Notes</h2>
    <ul>
        <li>The prompts are designed to return structured JSON output only.</li>
        <li>Sampling 100 reviews instead of 200 is due to free-tier API request limitations.</li>
        <li>The notebook saves prediction results and a comparison table for each prompting approach.</li>
    </ul>

    <h2>Acknowledgements</h2>
    <ul>
        <li>Google Gemini LLM (gemini-2.5-flash)</li>
        <li>Kaggle Yelp Reviews dataset</li>
    </ul>
</body>
</html>
