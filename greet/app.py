from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    """Show Homepage!"""

    return """<!DOCTYPE html><html lang="en">
    <body><h1>Index:</h1>
    <ul>
    <li><a href="/welcome">Welcome!</a></li>
    <li><a href="/welcome/home">Welcome home!</a></li>
    <li><a href="/welcome/back">Welcome back!</a></li>
    </ul>
    </body></html>"""


@app.route("/welcome")
def welcome():
    """Returns “welcome”"""
    return "<p>Welcome</p>"


@app.route("/welcome/home")
def welcome_home():
    """Returns “welcome home”"""
    return "<p>welcome home</p>"


@app.route("/welcome/back")
def welcome_back():
    """ Return “welcome back”"""
    return "<p>welcome back</p>"
