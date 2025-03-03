#!/usr/bin/python3
"""
Review API endpoints for HBnB
"""
from flask import request
from flask_restx import Namespace, Resource
from hbnb.app.models.review import Review
from hbnb.app.persistence.repository import review_repo, user_repo, place_repo

api = Namespace("reviews", description="Review management endpoints")

@api.route("/")
class ReviewList(Resource):
    def get(self):
        """Retrieve all reviews"""
        print("DEBUG: Entering GET /api/v1/reviews/")
        reviews = review_repo.get_all()
        return [
            {
                "id": r.id,
                "text": r.text,
                "rating": r.rating,
                "user_id": r.user_id,
                "place_id": r.place_id
            } for r in reviews
        ], 200

    def post(self):
        """Create a new review"""
        print("DEBUG: Entering POST /api/v1/reviews/")
        data = request.json

        required_fields = ["text", "rating", "user_id", "place_id"]
        for field in required_fields:
            if field not in data:
                return {"error": f"Missing required field: {field}"}, 400

        if not user_repo.get(data["user_id"]):
            return {"error": "User not found"}, 404

        if not place_repo.get(data["place_id"]):
            return {"error": "Place not found"}, 404

        new_review = Review(
            text=data["text"],
            rating=data["rating"],
            user_id=data["user_id"],
            place_id=data["place_id"]
        )
        review_repo.add(new_review)
        return {"message": "Review created", "id": new_review.id}, 201

@api.route("/<string:review_id>")
class ReviewDetail(Resource):
    def get(self, review_id):
        """Retrieve a specific review by ID"""
        print(f"DEBUG: Entering GET /api/v1/reviews/{review_id}")
        review = review_repo.get(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return {
            "id": review.id,
            "text": review.text,
            "rating": review.rating,
            "user_id": review.user_id,
            "place_id": review.place_id
        }, 200

    def put(self, review_id):
        """Update an existing review"""
        print(f"DEBUG: Entering PUT /api/v1/reviews/{review_id}")
        review = review_repo.get(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        data = request.json
        if "text" in data:
            review.text = data["text"]
        if "rating" in data:
            review.rating = data["rating"]

        review_repo.update(review_id, review)
        return {"message": "Review updated"}, 200

    def delete(self, review_id):
        """Delete a review"""
        print(f"DEBUG: Entering DELETE /api/v1/reviews/{review_id}")
        review = review_repo.get(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        review_repo.delete(review_id)
        return {"message": "Review deleted"}, 200