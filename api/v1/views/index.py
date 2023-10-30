#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def get_status():
    """return status"""
    return {"status": "OK"}


@app_views.route('/stats', strict_slashes=False)
def get_stats():
    """get stats count"""
    return {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
