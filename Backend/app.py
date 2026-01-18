from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home route
@app.route("/")
def home():
    return "Backend is running successfully"

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    hours = int(data["hours"])
    attendance = int(data["attendance"])
    previous = int(data["previous"])

    if hours < 5 or attendance < 60 or previous < 50:
        risk = "High Risk"
    elif hours < 10 or attendance < 75:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    return jsonify({"risk": risk})