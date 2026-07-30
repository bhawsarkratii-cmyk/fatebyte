from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

fortunes = [
    "Too glam to give a damn today. 💋✨",
    "You are going into your dream college! 😍",
    "Keep shining; it is blinding your haters. 😎✨",
    "Less perfection, way more authentic, gorgeous energy. 🔥💅",
    "Your vibe is expensive; act like it. 💎💅",
    "Manifesting miracles and massive checks for you. 💸✨",
    "You will meet someone special today 😊",
    "Something exciting is coming your way! ✨",
    "Good things take time. Keep going! 🌸",
    "Your hard work will pay off! 💫",
    "you will eat your favourite cheescake today",
    "Standardize your crown; you are ruling today. 👑✨",
    "You are the plot twist they needed. 😉🌟",

    
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
