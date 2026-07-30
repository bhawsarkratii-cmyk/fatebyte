from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

fortunes = [
    "You are going into your dream college! 😍",
    "You will meet someone special today 😊",
    "Something exciting is coming your way! ✨",
    "Good things take time. Keep going! 🌸",
    "Your hard work will pay off! 💫"
    "you will eat your favourite cheescake today"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fortune")
def fortune():
    return jsonify({
        "fortune": random.choice(fortunes)
    })

if __name__ == "__main__":
    app.run(debug=True)
