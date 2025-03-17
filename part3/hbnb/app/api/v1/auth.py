#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from hbnb.app.services.facade import get_facade
from flask import jsonify
import json

api = Namespace('auth', description='Authentication operations')

# Model for input validation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})


@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token"""
        try:
            credentials = api.payload
            facade = get_facade()

            # Ensure both email and password are provided
            if not credentials or 'email' not in credentials or 'password' not in credentials:
                return {'error': 'Email and password are required'}, 400

            # Step 1: Retrieve the user based on the provided email
            user = facade.get_user_by_email(credentials['email'])

            # Step 2: Check if the user exists and verify the password
            if not user or not user.check_password(credentials['password']):
                return {'error': 'Invalid email or password'}, 401

            # Step 3: Create a JWT token with the user's id and is_admin flag
            identity_data = json.dumps({"id": str(user.id), "is_admin": user.is_admin})
            access_token = create_access_token(identity=identity_data)


            # Step 4: Return the JWT token to the client
            return {'access_token': access_token}, 200

        except Exception as e:
            return {'error': f'Internal Server Error: {str(e)}'}, 500


@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        """A protected endpoint that requires a valid JWT token"""
        current_user = json.loads(get_jwt_identity())
        return {'message': f'Hello, user {current_user["id"]}', 'is_admin': current_user["is_admin"]}, 200
    
        
        if not isinstance(current_user, dict) or 'id' not in current_user:
            return {"error": "Invalid token format"}, 400

        return {"message": f"Hello, user {current_user['id']}", "is_admin": current_user["is_admin"]}, 200
    


@api.route('/logout')
class Logout(Resource):
    @jwt_required()
    def post(self):
        """Logout user (token revocation not implemented yet)"""
        return {'message': 'Logout successful'}, 200