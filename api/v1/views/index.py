#!/usr/bin/python3
""" create a route on the object app_views
that returns a JSON: status: OK """
from flask import Flask, Blueprint, jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def _status():
    """ return a JSON file with Status: OK """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_clashes=False)
def stats():
    """ Create an end point that retrieves the no. of each objects by type """
    countAmenity = storage.count("Amenity")
    countCities = storage.count("City")
    countPlaces = storage.count("Place")
    countReviews = storage.count("Review")
    countStates = storage.count("State")
    countUsers = storage.count("User")
    return jsonify(amenities=countAmenity,
                   cities=countCities,
                   places=countPlaces,
                   reviews=countReviews,
                   states=countStates,
                   users=countUsers)
