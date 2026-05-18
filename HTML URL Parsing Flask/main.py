from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess/<name>")
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    age = age_data["age"]

    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    return render_template("age.html", name=name, age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts, num=int(num))

if __name__ == "__main__":
    app.run(debug=True)