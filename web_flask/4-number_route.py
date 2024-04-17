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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_text_p(text="is cool"):
    """display text"""
    txt = text.replace("_", " ")
    return f"Python {txt}"


@app.route("/number/<int:n>")
def number(n):
    """display number"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
