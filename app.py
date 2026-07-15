import random
import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

COMPLIMENTS = [
    "You have an amazing sense of humor!",
    "Your positivity is infectious.",
    "You're a fantastic problem solver.",
    "That's a wonderful idea!",
    "You are incredibly resourceful.",
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-compliment")
def get_compliment():
    selected = random.choice(COMPLIMENTS)
    return jsonify({"compliment": selected})

if __name__ == "__main__":
    # Binds to the dynamic port assigned by Railway
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)