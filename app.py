from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "messages.json"

def load_messages():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_message(message):
    data = load_messages()
    data.append(message)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    data = request.json

    message = {
        "name": data.get("name"),
        "email": data.get("email"),
        "message": data.get("message")
    }

    save_message(message)

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
