#!/usr/bin/python3
"""
Place API endpoints for HBnB
"""
from flask import request
from flask_restx import Namespace, Resource
from hbnb.app.models.place import Place
from hbnb.app.persistence.repository import place_repo, user_repo, amenity_repo

api = Namespace("places", description="Place management endpoints")

@api.route("/")
class PlaceList(Resource):
    def get(self):
        """Retrieve all places"""
        print("DEBUG: Entering GET /api/v1/places/")
        places = place_repo.get_all()
        return [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "latitude": p.latitude,
                "longitude": p.longitude,
                "owner_id": p.owner_id,
                "amenities": [a.id for a in p.amenities]
            } for p in places
        ], 200

    def post(self):
        """Create a new place"""
        print("DEBUG: Entering POST /api/v1/places/")
        data = request.json

        required_fields = ["name", "price", "latitude", "longitude", "owner_id"]
        for field in required_fields:
            if field not in data:
                return {"error": f"Missing required field: {field}"}, 400

        if not user_repo.get(data["owner_id"]):
            return {"error": "Owner user not found"}, 404

        new_place = Place(
            name=data["name"],
            price=data["price"],
            latitude=data["latitude"],
            longitude=data["longitude"],
            owner_id=data["owner_id"]
        )
        place_repo.add(new_place)
        return {"message": "Place created", "id": new_place.id}, 201

@api.route("/<string:place_id>")
class PlaceDetail(Resource):
    def get(self, place_id):
        """Retrieve a specific place by ID"""
        print(f"DEBUG: Entering GET /api/v1/places/{place_id}")
        place = place_repo.get(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        return {
            "id": place.id,
            "name": place.name,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner_id": place.owner_id,
            "amenities": [a.id for a in place.amenities]
        }, 200

    def put(self, place_id):
        """Update an existing place"""
        print(f"DEBUG: Entering PUT /api/v1/places/{place_id}")
        place = place_repo.get(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        data = request.json
        if "name" in data:
            place.name = data["name"]
        if "price" in data:
            place.price = data["price"]
        if "latitude" in data:
            place.latitude = data["latitude"]
        if "longitude" in data:
            place.longitude = data["longitude"]

        place_repo.update(place_id, place)
        return {"message": "Place updated"}, 200