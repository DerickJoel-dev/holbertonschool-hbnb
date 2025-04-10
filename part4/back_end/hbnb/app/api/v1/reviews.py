#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from hbnb.app.services.facade import get_facade
import json

facade = get_facade()

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/', strict_slashes=False)
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        current_user_data = json.loads(current_user) if isinstance(current_user, str) else current_user
        review_data = api.payload

        if current_user_data.get('id') != review_data['user_id']:
            return {'error': 'Unauthorized action'}, 403

        place = facade.get_place(review_data['place_id'])
        if place and place.owner_id == current_user_data.get('id'):
            return {'error': 'You cannot review your own place.'}, 400

        reviews = facade.get_reviews_by_place(review_data['place_id'])
        for review in reviews:
            if review.user_id == current_user_data.get('id'):
                return {'error': 'You have already reviewed this place.'}, 400

        try:
            new_review = facade.create_review(review_data)
            return {
                'id': new_review.id,
                'text': new_review.text,
                'rating': new_review.rating,
                'user_id': new_review.user_id,
                'place_id': new_review.place_id
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        reviews = facade.get_all_reviews()
        return [{
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'user_id': review.user_id,
            'place_id': review.place_id
        } for review in reviews], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return {
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'user_id': review.user_id,
            'place_id': review.place_id
        }, 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def put(self, review_id):
        current_user = get_jwt_identity()
        current_user_data = json.loads(current_user) if isinstance(current_user, str) else current_user
        review_data = api.payload

        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        if current_user_data.get('id') != review.user_id:
            return {'error': 'Unauthorized action'}, 403

        updated_review = facade.update_review(review_id, review_data)
        return {
            'text': updated_review.text,
            'rating': updated_review.rating
        }, 200

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized action')
    @jwt_required()
    def delete(self, review_id):
        current_user = get_jwt_identity()
        current_user_data = json.loads(current_user) if isinstance(current_user, str) else current_user

        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404

        if current_user_data.get('id') != review.user_id:
            return {'error': 'Unauthorized action'}, 403

        facade.delete_review(review_id)
        return {'message': 'Review deleted successfully'}, 200

@api.route('/places/<string:place_id>/reviews', strict_slashes=False)
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    def get(self, place_id):
        reviews = facade.get_reviews_by_place(place_id)
        return [{
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'user_id': review.user_id,
            'place_id': review.place_id
        } for review in reviews], 200
