#!/usr/bin/python3
from hbnb.app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, owner_id, name, latitude, longitude, description="", price=0.0):
        super().__init__()
        self.owner_id = owner_id  # ID de un User
        self.name = self._validate_name(name)
        self.latitude = self._validate_latitude(latitude)
        self.longitude = self._validate_longitude(longitude)
        self.description = description
        self.price = self._validate_price(price)
        self.amenities = []  # 🔹 Esto soluciona el error

    def _validate_name(self, name):
        if not name:
            raise ValueError("Place name cannot be empty")
        return name

    def _validate_price(self, price):
        price = float(price)
        if price < 0:
            raise ValueError("Price cannot be negative")
        return price

    def _validate_latitude(self, latitude):
        latitude = float(latitude)
        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude must be between -90 and 90")
        return latitude

    def _validate_longitude(self, longitude):
        longitude = float(longitude)
        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude must be between -180 and 180")
        return longitude