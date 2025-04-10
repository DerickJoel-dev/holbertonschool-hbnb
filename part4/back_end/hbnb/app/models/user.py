#!/usr/bin/python3

from hbnb.app.models.base_model import BaseModel
from hbnb.app import db, bcrypt
import uuid

class User(BaseModel, db.Model):
    
    __tablename__ = 'users'
    
    id = db.Column(db.String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        self.is_admin = is_admin

    def set_password(self, password):
        """Hash the password using Flask-Bcrypt"""
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Verify if the provided password matches the stored hash"""
        return bcrypt.check_password_hash(self.password_hash, password)

    def _validate_name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        return name

    def _validate_email(self, email):
        if "@" not in email:
            raise ValueError("Invalid email format")
        return email
    
    def to_dict(self):
        """Convert user object to dictionary, hiding sensitive data"""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }
