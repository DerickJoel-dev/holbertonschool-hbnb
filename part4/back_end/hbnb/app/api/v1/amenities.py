#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from hbnb.app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload

        if 'name' not in amenity_data:
            return {'error': 'Invalid input data'}, 400

        new_amenity = facade.create_amenity(amenity_data)
        return {
            'id': new_amenity.id,
            'name': new_amenity.name
        }, 201

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve all amenities"""
        amenities = facade.get_all_amenities()
        return [{
            'id': amenity.id,
            'name': amenity.name
        } for amenity in amenities], 200


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404

        return {
            'id': amenity.id,
            'name': amenity.name
        }, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, amenity_id):
        """Update an amenity"""
        amenity_data = api.payload

        if not amenity_data.get('name'):
            return {'error': 'Amenity name is required'}, 400

        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404

        updated_amenity = facade.update_amenity(amenity_id, amenity_data)
        return {
            'message': 'Amenity updated successfully',
            'amenity': {
                'id': updated_amenity.id,
                'name': updated_amenity.name
            }
        }, 200

    @api.response(200, 'Amenity deleted successfully')
    @api.response(404, 'Amenity not found')
    @jwt_required()
    def delete(self, amenity_id):
        """Delete an amenity by ID"""
        if facade.delete_amenity(amenity_id):
            return {'message': 'Amenity deleted successfully'}, 200

        return {'error': 'Amenity not found'}, 404
