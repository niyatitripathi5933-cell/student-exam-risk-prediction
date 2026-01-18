from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --------------------------
# Homepage route (404 fix)
# --------------------------
@app.route("/")
def home():
    return "Backend is running successfully"

# --------------------------
# Example predict route
# --------------------------
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Data validation
    try:
        hours = int(data.get('hours', 0))
        attendance = int(data.get('attendance', 0))
        previous = int(data.get('previous', 0))
    except:
        return jsonify({"error": "Invalid input"}), 400

    # Example prediction logic (replace with your ML model later)
    # Simple example: prediction = hours + attendance + previous
    prediction = hours * 0.5 + attendance * 0.3 + previous * 0.2

    return jsonify({"prediction": round(prediction, 2)})

# -------------------------------------------------
# Note: Do NOT include app.run() for Render
# Gunicorn automatically starts the server
# -------------------------------------------------
