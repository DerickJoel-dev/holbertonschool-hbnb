#!/usr/bin/python3

from flask import Flask, jsonify
from flask_restx import Api
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
jwt = JWTManager()

# namespaces
from hbnb.app.api.v1.users import api as users_ns
from hbnb.app.api.v1.amenities import api as amenity_ns
from hbnb.app.api.v1.places import api as place_ns
from hbnb.app.api.v1.reviews import api as review_ns
from hbnb.app.api.v1.auth import api as auth_ns

# Set revoked tokens
revoked_tokens = set()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #  Configure CORS before anything else
    CORS(
        app,
        resources={r"/api/*": {"origins": ["http://127.0.0.1:5500"]}},
        supports_credentials=True,
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization"]
    )

    #  Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    #  Auth JWT config
    authorizations = {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    }

    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        authorizations=authorizations,
        security="BearerAuth",
    )

    #  Register namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    api.add_namespace(place_ns, path="/api/v1/places")
    api.add_namespace(review_ns, path="/api/v1/reviews")
    api.add_namespace(auth_ns, path="/api/v1/auth")

    #  JWT token expired callback
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({"message": "Token has expired", "error": "token_expired"}), 401

    #  JWT token blacklist (logout)
    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload):
        return jwt_payload["jti"] in revoked_tokens

    return app
