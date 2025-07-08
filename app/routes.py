from app import app
from flask import render_template
from app.projects import projects
from flask import request

def get_project_by_slug(slug):
    for project in projects:
        if project["slug"] == slug:
            return project
    return None


@app.route("/")
def index():
    return render_template("index.html", request=request)

@app.route("/skills")
def skills():
    return render_template("skills.html", request=request)

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects, request=request)

@app.route("/music")
def music():
    return render_template("music.html", request=request)

@app.route("/contact")
def contact():
    return render_template("contact.html", request=request)

@app.route("/projects/<slug>")
def project_detail(slug):
    project = get_project_by_slug(slug)
    if not project:
        return "Project not found", 404
    return render_template("project_detail.html", project=project)