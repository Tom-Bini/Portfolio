from app import app
from flask import render_template
from app.projects import projects

def get_project_by_slug(slug):
    for project in projects:
        if project["slug"] == slug:
            return project
    return None


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/projects/<slug>")
def project_detail(slug):
    project = get_project_by_slug(slug)
    if not project:
        return "Project not found", 404
    return render_template("project_detail.html", project=project)