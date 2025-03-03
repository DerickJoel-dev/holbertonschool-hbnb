#!/usr/bin/python3
"""
User API endpoints for HBnB - Task 2
"""
from flask import request
from flask_restx import Namespace, Resource
from hbnb.app.models.user import User
from hbnb.app.persistence.repository import user_repo

api = Namespace("users", description="User management endpoints")

@api.route("/")
class UserList(Resource):
    def get(self):
        """Retrieve all users"""
        print("DEBUG: Entering GET /api/v1/users/")
        users = user_repo.get_all()
        print("DEBUG: Users in memory:", users)
        return [
            {
                "id": u.id,
                "first_name": u.first_name,
                "last_name": u.last_name,
                "email": u.email
            } for u in users
        ], 200

    def post(self):
        """Create a new user"""
        print("DEBUG: Entering POST /api/v1/users/")
        data = request.json
        try:
            new_user = User(
                data["first_name"],
                data["last_name"],
                data["email"],
                data["password"]
            )
            user_repo.add(new_user)
            return {"message": "User created", "id": new_user.id}, 201
        except KeyError as e:
            return {"error": f"Missing key: {str(e)}"}, 400
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            print("DEBUG: Unhandled exception:", e)
            return {"error": "Server error"}, 500

@api.route("/<string:user_id>")
class UserDetail(Resource):
    def get(self, user_id):
        """Retrieve a user by ID"""
        print(f"DEBUG: Entering GET /api/v1/users/{user_id}")
        user = user_repo.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }, 200

    def put(self, user_id):
        """Update an existing user"""
        print(f"DEBUG: Entering PUT /api/v1/users/{user_id}")
        user = user_repo.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        data = request.json
        user.first_name = data.get("first_name", user.first_name)
        user.last_name = data.get("last_name", user.last_name)
        user.email = data.get("email", user.email)

        user_repo.update(user_id, user)
        return {"message": "User updated"}, 200