#!/usr/bin/python3
from hbnb.app.models.base_model import BaseModel
from hbnb.app import db

place_amenity = db.Table(
    'place_amenity',
    db.Column('place_id', db.String(60), db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String(60), db.ForeignKey('amenities.id'), primary_key=True),
    extend_existing=True
)

class Place(BaseModel, db.Model):  
    __tablename__ = 'places'
    
    id = db.Column(db.String(60), primary_key=True)
    owner_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)  
    name = db.Column(db.String(128), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False, default=0.0)
    amenities = db.relationship('Amenity', secondary='place_amenity', backref='places', lazy=True)  

    def __init__(self, owner_id, name, latitude, longitude, description="", price=0.0, amenities=None):
        super().__init__()
        self.owner_id = owner_id
        self.name = self._validate_name(name)
        self.latitude = self._validate_latitude(latitude)
        self.longitude = self._validate_longitude(longitude)
        self.description = description
        self.price = self._validate_price(price)
        self.amenities = amenities if amenities else []

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
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,  
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "amenities": [amenity.id for amenity in self.amenities] if self.amenities else []
        }
