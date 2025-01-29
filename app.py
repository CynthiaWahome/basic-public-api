from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

import os
import platform
import random

class Config:
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable

def get_quotes():
    return [
        "Keep pushing forward! 🚀",
        "Success is the sum of small efforts repeated daily. 🔥",
        "The best way to predict the future is to create it. 💡",
        "The only limit is your mind. 🤯",
        "Good things take time. Be patient. 🌟",
    ]

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)  # Enable CORS

@app.route("/", methods=["GET"])
def home():
    response = {
        "email": os.getenv("EMAIL"),
        "current_datetime": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",  # ISO 8601 UTC
        "github_url": "https://github.com/CynthiaWahome/basic-public-api.git",
        "track": "Backend",
        "server_info": {
            "os": platform.system(),
            "python_version": platform.python_version()
        },
        "message": random.choice(get_quotes())
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"])
