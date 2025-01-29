commifrom flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/", methods=["GET"])
def home():
    response = {
        "email": "your-email@example.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",  # ISO 8601 UTC
        "github_url": "https://github.com/CynthiaWahome/basic-public-api.git"
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
