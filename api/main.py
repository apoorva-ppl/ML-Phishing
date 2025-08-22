

from flask import Flask, request, render_template
import joblib
import numpy as np
import sys
import os

# This is important to find your feature_extractor.py file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from feature_extractor import extract_features

app = Flask(__name__, template_folder='../frontend/templates')

# Load your trained phishing model
model = joblib.load('../phishing_detector.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url = request.form['url']

        # Extract features and reshape for the model
        url_features = np.array(extract_features(url)).reshape(1, -1)

        # Make a prediction
        prediction = model.predict(url_features)

        # Interpret the result
        result = "Malicious URL (Phishing)" if prediction[0] == 1 else "Safe URL (Benign)"

        return render_template('index.html', prediction_text=result, url_checked=url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
