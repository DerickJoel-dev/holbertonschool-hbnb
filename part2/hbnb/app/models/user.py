#!/usr/bin/python3
from hbnb.app.models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, password):
        super().__init__()
        self.first_name = self._validate_name(first_name)
        self.last_name = self._validate_name(last_name)
        self.email = self._validate_email(email)
        self.password = self._validate_password(password)

    def _validate_name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        return name

    def _validate_email(self, email):
        if "@" not in email:
            raise ValueError("Invalid email format")
        return email

    def _validate_password(self, password):
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")
        return password