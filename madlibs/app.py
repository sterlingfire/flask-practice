from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# silly_story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time, in a long-ago {place}, there lived an exceptionally
#        {adjective} {noun}. It loved to {verb} with {plural_noun}."""
# )


@app.route("/")
def view_index():
    """Create form to generate Madlibs story"""
    return render_template("questions.html",
                           story=silly_story)


@app.route("/results")
def show_story():
    return render_template("story.html", story=silly_story)
