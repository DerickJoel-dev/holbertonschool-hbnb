#!/usr/bin/python3

from flask import flask
from flask_restx import Api
from api.routes.users import user_ns
from api.routes.places import place_ns
from api.routes.reviews import review_ns
from api.routes.amenities import amenity_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, title="HBnB API", version="1.0", description="HBnB API Documentation")
    
    
    api.add_namespace(user_ns, path="/api/v1/users")
    api.add_namespace(place_ns, path="/api/v1/places")
    api.add_namespace(review_ns, path="/api/v1/reviews")
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    
    return app