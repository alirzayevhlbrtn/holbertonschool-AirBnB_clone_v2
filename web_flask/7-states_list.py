#!/usr/bin/python3
"""
script for storage
"""
from flask import Flask
from Flask import render_template
from models import storage

app = Flask(__name__)


@app.route("states_list", strict_slashes=False)
def states_list():
    """code goes here"""
    states = storage.all("State").values()
    s_states = sorted(states, key=lambda x: x.name)
    return render_template("7-states_list.html", st=s_states)


@app.teardown_appcontext
def teardown(exc):
    """destroy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")