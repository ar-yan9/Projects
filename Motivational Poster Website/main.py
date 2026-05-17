from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

quotes = [
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"text": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
    {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"text": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
    {"text": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein"},
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"text": "It always seems impossible until it's done.", "author": "Nelson Mandela"},
]

backgrounds = [
    "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1200",
    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1200",
    "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?w=1200",
    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1200",
    "https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?w=1200",
]

@app.route("/")
def home():
    quote = random.choice(quotes)
    background = random.choice(backgrounds)
    return render_template("index.html", quote=quote, background=background)

if __name__ == "__main__":
    app.run(debug=True)