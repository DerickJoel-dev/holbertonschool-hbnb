#!/usr/bin/python3

from hbnb.app.models.base_model import BaseModel
from hbnb.app import db


place_amenity = db.Table(
    'place_amenity',
    db.Column('place_id', db.String(60), db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String(60), db.ForeignKey('amenities.id'), primary_key=True)
)

class Amenity(BaseModel, db.Model):
    """Defines the Amenity model for the HBnB project"""
    
    __tablename__ = 'amenities'

    id = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)

    def __repr__(self):
        return f"<Amenity(id='{self.id}', name='{self.name}')>"