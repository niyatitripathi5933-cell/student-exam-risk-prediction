from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    hours = int(data['hours'])
    attendance = int(data['attendance'])
    previous = int(data['previous'])

    if hours < 5 or attendance < 60 or previous < 50:
        risk = "High Risk"
    elif hours < 10 or attendance < 75:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    return jsonify({"risk": risk})

# Serve frontend files
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def serve_frontend(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)