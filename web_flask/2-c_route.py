#!/usr/bin/python3
"""
task 0
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """default page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """say hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """display text"""
    txt = text.replace("_", " ")
    return f"C {txt}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
