#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from hbnb.app.services.facade import get_facade
import json
from hbnb.app import db

facade = get_facade()

api = Namespace('places', description='Place operations')

amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

place_model = api.model('Place', {
    'name': fields.String(required=True, description='Name of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's"),
    'reviews': fields.List(fields.Nested(review_model), description="List of reviews")
})

@api.route('/', strict_slashes=False)
class PlaceList(Resource):
    @api.response(200, 'List of all places')
    @jwt_required()
    def get(self):
        places = facade.get_all_places()
        return [
            {
                'id': place.id,
                'name': place.name,
                'price_per_night': place.price  # importante que el nombre coincida con scripts.js
            }
            for place in places
        ], 200


@api.route('/<place_id>', strict_slashes=False)
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        place = facade.get_place(str(place_id))
        if not place:
            return {'error': 'Place not found'}, 404
        return {
            'id': place.id,
            'name': place.name,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner_id': place.owner_id,
            'amenities': [
                {'id': amenity.id, 'name': amenity.name} for amenity in place.amenities
            ] if place.amenities else []
        }, 200

@api.route('/<place_id>/amenities', strict_slashes=False)
class PlaceAmenities(Resource):
    @api.expect(api.model('PlaceAmenity', {
        'amenity_id': fields.String(required=True, description="ID of the amenity")
    }))
    @api.response(201, "Amenity successfully added to place")
    @api.response(404, "Place or Amenity not found")
    @api.response(400, "Invalid input data")
    @jwt_required()
    def post(self, place_id):
        current_user = get_jwt_identity()
        amenity_data = api.payload

        place = facade.get_place(str(place_id))
        if not place:
            return {"error": "Place not found"}, 404

        amenity = facade.get_amenity(amenity_data["amenity_id"])
        if not amenity:
            return {"error": "Amenity not found"}, 404

        place.amenities.append(amenity)
        db.session.commit()

        return {"message": "Amenity successfully added to place"}, 201
