#!/usr/bin/python3

from hbnb.app.persistence.repository import user_repo, amenity_repo, place_repo, review_repo
from hbnb.app.models.user import User
from hbnb.app.models.amenity import Amenity
from hbnb.app.models.place import Place
from hbnb.app.models.review import Review
from hbnb.app import db

class HBnBFacade:
    def create_user(self, user_data):
        user = User(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            password=user_data['password']  
        )  
        user.set_password(user_data['password']) 
        user_repo.add(user)
        return user

    def get_user(self, user_id):
        return user_repo.get(user_id)

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_all_users(self):
        return user_repo.get_all()

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if amenity:
            for key, value in amenity_data.items():
                setattr(amenity, key, value)
            return amenity
        return None

    def create_place(self, place_data):
        owner = user_repo.get(place_data['owner_id'])
        if not owner:
            raise ValueError("Invalid owner ID")

        amenities = [amenity_repo.get(aid) for aid in place_data['amenities']]
        if None in amenities:
            raise ValueError("Invalid amenity ID in amenities list")

        place = Place(
            name=place_data['name'],
            description=place_data.get('description', ''),
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner_id=owner.id, 
            amenities=amenities
        )
        place_repo.add(place)
        return place

    def get_place(self, place_id):
        return place_repo.get(place_id)
    
    def get_all_places(self):
        return Place.query.all()



    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if place:
            for key, value in place_data.items():
                setattr(place, key, value)
                db.session.commit()
            return place
        return None

    def delete_place(self, place_id):
        place = self.get_place(place_id)
        if place:
            place_repo.delete(place_id)
            return True
        return False

    def create_review(self, review_data):
        user = user_repo.get(review_data['user_id'])
        place = place_repo.get(review_data['place_id'])

        if not user or not place:
            raise ValueError("Invalid user or place ID")

        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            user_id=user.id,
            place_id=place.id
        )
        review_repo.add(review)
        return review

    def get_review(self, review_id):
        return review_repo.get(review_id)

    def get_all_reviews(self):
        return review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return [review for review in self.get_all_reviews() if review.place_id == place_id]

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        if review:
            for key, value in review_data.items():
                setattr(review, key, value)
            db.session.commit()
            return review
        return None

    def delete_review(self, review_id):
        review = self.get_review(review_id)
        if review:
            review_repo.delete(review_id)
            db.session.commit()
            return True
        return False

def get_facade():
    return HBnBFacade()
