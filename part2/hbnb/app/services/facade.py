#!/usr/bin/python3

from persistence.repository import InMemoryRepository

class HbnbFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # ---------- USER METHODS ----------
    def add_user(self, user):
        return self.user_repo.add(user)

    def get_user(self, user_id):
        user = self.user_repo.get(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def get_all_users(self):
        return self.user_repo.get_all()

    def delete_user(self, user_id):
        if not self.user_repo.delete(user_id):
            raise ValueError("User not found")
        return True

    # ---------- PLACE METHODS ----------
    def add_place(self, place):
        return self.place_repo.add(place)

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")
        return place

    def get_all_places(self):
        return self.place_repo.get_all()

    def delete_place(self, place_id):
        if not self.place_repo.delete(place_id):
            raise ValueError("Place not found")
        return True

    # ---------- REVIEW METHODS ----------
    def add_review(self, review):
        return self.review_repo.add(review)

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review not found")
        return review

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def delete_review(self, review_id):
        if not self.review_repo.delete(review_id):
            raise ValueError("Review not found")
        return True

    # ---------- AMENITY METHODS ----------
    def add_amenity(self, amenity):
        return self.amenity_repo.add(amenity)

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            raise ValueError("Amenity not found")
        return amenity

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def delete_amenity(self, amenity_id):
        if not self.amenity_repo.delete(amenity_id):
            raise ValueError("Amenity not found")
        return True