from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story_templates

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def show_template_picker():
    return render_template("story_templates.html",
                           templates=story_templates)


@app.route("/input")
def view_index():
    """Create form to generate Madlibs story"""
    story_name = request.args.get("template_picker")
    return render_template("questions.html",
                           story=story_templates[story_name],
                           story_name=story_name)


@app.route("/results")
def show_story():
    """ Display the story from the form data"""
    story_name =request.args.get("story_name")
    story_text = story_templates[story_name].generate(request.args)
    return render_template("story.html", story=story_text)
