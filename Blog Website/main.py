from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    blog_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", all_posts=all_posts)

@app.route("/post/<int:index>")
def get_post(index):
    blog_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(blog_url)
    all_posts = response.json()
    requested_post = all_posts[index - 1]
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)