from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# etc. pour /skills, /projects, etc.
