from hbnb.app.models.base_model import BaseModel

class Review(BaseModel):
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
