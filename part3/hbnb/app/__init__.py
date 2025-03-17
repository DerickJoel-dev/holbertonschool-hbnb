#!/usr/bin/python3

from flask import Flask, jsonify
from flask_restx import Api
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
jwt = JWTManager()

#  namespaces
from hbnb.app.api.v1.users import api as users_ns
from hbnb.app.api.v1.amenities import api as amenity_ns
from hbnb.app.api.v1.places import api as place_ns
from hbnb.app.api.v1.reviews import api as review_ns
from hbnb.app.api.v1.auth import api as auth_ns  # Agregamos autenticación

# Set revoked tokens
revoked_tokens = set()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initialize extensions with the app
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # auth jwt
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

    # namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenity_ns, path="/api/v1/amenities")
    api.add_namespace(place_ns, path="/api/v1/places")
    api.add_namespace(review_ns, path="/api/v1/reviews")
    api.add_namespace(auth_ns, path="/api/v1/auth")

    #  tokens expired
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({"message": "Token has expired", "error": "token_expired"}), 401

    # handling revoked tokens (logout)
    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload):
        return jwt_payload["jti"] in revoked_tokens

    return app