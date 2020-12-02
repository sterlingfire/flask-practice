from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def view_index():
    """Renders Index.html"""
    return render_template(something) # Needs work
