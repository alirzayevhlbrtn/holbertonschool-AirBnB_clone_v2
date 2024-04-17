#!/usr/bin/python3
"""
task 0
"""
from flask import Flask
from flask import render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display number"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display number"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """display number"""
    if n % 2 == 0:
        ort = "even"
    else:
        ort = "odd"
    return render_template("6-number_odd_or_even.html", n=n, ort=ort)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
