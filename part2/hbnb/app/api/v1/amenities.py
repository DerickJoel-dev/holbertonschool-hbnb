#!/usr/bin/python3
"""
Amenity API endpoints for HBnB
"""
from flask import request
from flask_restx import Namespace, Resource
from hbnb.app.models.amenity import Amenity
from hbnb.app.persistence.repository import amenity_repo

api = Namespace("amenities", description="Amenity management endpoints")

@api.route("/")
class AmenityList(Resource):
    def get(self):
        """Retrieve all amenities"""
        print("DEBUG: Entering GET /api/v1/amenities/")
        amenities = amenity_repo.get_all()
        return [{"id": a.id, "name": a.name} for a in amenities], 200

    def post(self):
        """Create a new amenity"""
        print("DEBUG: Entering POST /api/v1/amenities/")
        data = request.json

        if not data or "name" not in data:
            return {"error": "Missing required field: name"}, 400

        new_amenity = Amenity(data["name"])
        amenity_repo.add(new_amenity)
        return {"message": "Amenity created", "id": new_amenity.id}, 201

@api.route("/<string:amenity_id>")
class AmenityDetail(Resource):
    def get(self, amenity_id):
        """Retrieve a specific amenity by ID"""
        print(f"DEBUG: Entering GET /api/v1/amenities/{amenity_id}")
        amenity = amenity_repo.get(amenity_id)
        if not amenity:
            return {"error": "Amenity not found"}, 404
        return {"id": amenity.id, "name": amenity.name}, 200

    def put(self, amenity_id):
        """Update an existing amenity"""
        print(f"DEBUG: Entering PUT /api/v1/amenities/{amenity_id}")
        amenity = amenity_repo.get(amenity_id)
        if not amenity:
            return {"error": "Amenity not found"}, 404

        data = request.json
        if "name" in data:
            amenity.name = data["name"]
            amenity_repo.update(amenity_id, amenity)

        return {"message": "Amenity updated"}, 200
