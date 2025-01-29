from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

import os

class Config:
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)  # Enable CORS

@app.route("/", methods=["GET"])
def home():
    response = {
        "email": os.getenv("EMAIL"),
        "current_datetime": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",  # ISO 8601 UTC
        "github_url": "https://github.com/CynthiaWahome/basic-public-api"
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"])
