from app import app
from flask import render_template
from projects import projects


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

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/projects/<slug>')
def project_detail(slug):
    project = get_project_by_slug(slug)  # fonction à toi
    if project:
        return render_template("project_detail.html", project=project)
    else:
        abort(404)