#!/usr/bin/python3

from hbnb.app.models.base_model import BaseModel
from hbnb.app import db

class Review(BaseModel, db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.String(60), primary_key=True)
    text = db.Column(db.String(1024), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    place_id = db.Column(db.String(60), db.ForeignKey('places.id'), nullable=False)

    user = db.relationship('User', backref='reviews')
    place = db.relationship('Place', backref='reviews')

    def __init__(self, text, rating, user_id, place_id):
        super().__init__()
        self.text = self._validate_text(text)
        self.rating = self._validate_rating(rating)
        self.user_id = user_id
        self.place_id = place_id

    def _validate_text(self, text):
        if not text:
            raise ValueError("Review text cannot be empty")
        return text

    def _validate_rating(self, rating):
        rating = int(rating)
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        return rating

    def __repr__(self):
        return f"<Review(id='{self.id}', text='{self.text}', rating='{self.rating}')>"
