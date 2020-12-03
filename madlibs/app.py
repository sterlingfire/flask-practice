from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def view_index():
    """Create form to generate Madlibs story"""
    return render_template("questions.html",
                           story=silly_story)


@app.route("/results")
def show_story():
    """ Display the story from the form data"""

    story_text = silly_story.generate(request.args)
    return render_template("story.html", story=story_text)
