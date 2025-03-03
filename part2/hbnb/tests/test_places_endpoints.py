#!/usr/bin/python3
"""Unit tests for Place API endpoints"""

import unittest
import json
from hbnb.app import create_app

class TestPlaceEndpoints(unittest.TestCase):
    """Test cases for Place endpoints"""

    def setUp(self):
        """Set up test client"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.test_place = {"name": "Beach House", "city_id": "test-city-id"}

    def test_get_all_places(self):
        """Test GET /api/v1/places"""
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)

    def test_create_place(self):
        """Test POST /api/v1/places with valid data"""
        response = self.client.post('/api/v1/places/',
                                    data=json.dumps(self.test_place),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_place_invalid(self):
        """Test POST /api/v1/places with missing data"""
        response = self.client.post('/api/v1/places/',
                                    data=json.dumps({"name": "Empty Place"}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()