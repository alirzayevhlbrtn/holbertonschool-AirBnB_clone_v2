#!/usr/bin/python3
"""Flask Project"""
from models.__init__ import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display a HTML page like in 6-index.html."""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)

    for state in states:
        state.cities = sorted(state.cities, key=lambda x: x.name)

    return render_template(
        "10-hbnb_filters.html",
        states=states,
        amenities=amenities,
    )



@app.teardown_appcontext
def teardown(exc):
    """Remove session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
