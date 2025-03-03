#!/usr/bin/python3
"""Unit tests for Review API endpoints"""

import unittest
import json
from hbnb.app import create_app

class TestReviewEndpoints(unittest.TestCase):
    """Test cases for Review endpoints"""

    def setUp(self):
        """Set up test client"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.test_review = {"text": "Great place!", "user_id": "user-123", "place_id": "place-123"}

    def test_get_all_reviews(self):
        """Test GET /api/v1/reviews"""
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)

    def test_create_review(self):
        """Test POST /api/v1/reviews with valid data"""
        response = self.client.post('/api/v1/reviews/',
                                    data=json.dumps(self.test_review),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_review_invalid(self):
        """Test POST /api/v1/reviews with missing text"""
        response = self.client.post('/api/v1/reviews/',
                                    data=json.dumps({"user_id": "user-123"}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()