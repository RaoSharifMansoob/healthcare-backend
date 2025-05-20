from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Allow requests from your frontend

# Load your trained model (make sure the path is correct)
model = joblib.load("random_forest_brute_force_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # You must ensure the frontend sends these values
    features = [
        data.get("login_status", 0),
        data.get("hour", 12),
        data.get("user_agent_score", 0.5)
    ]

    prediction = model.predict([features])[0]

    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(port=5000)
