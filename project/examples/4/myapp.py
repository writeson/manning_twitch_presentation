from flask import render_template
from app import create_app


app = create_app()
app.logger.info("MyBlog is running")


@app.get("/")
def home():
    return render_template("home/index.html")


@app.get("/content")
def content():
    return render_template("content/index.html")
