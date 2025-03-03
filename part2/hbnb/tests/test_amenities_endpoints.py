#!/usr/bin/python3
"""Unit tests for Amenity API endpoints"""

import unittest
import json
from hbnb.app import create_app

class TestAmenityEndpoints(unittest.TestCase):
    """Test cases for Amenity endpoints"""

    def setUp(self):
        """Set up test client"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.test_amenity = {"name": "Swimming Pool"}

    def test_get_all_amenities(self):
        """Test GET /api/v1/amenities"""
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)

    def test_create_amenity(self):
        """Test POST /api/v1/amenities with valid data"""
        response = self.client.post('/api/v1/amenities/',
                                    data=json.dumps(self.test_amenity),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_amenity_invalid(self):
        """Test POST /api/v1/amenities with missing name"""
        response = self.client.post('/api/v1/amenities/',
                                    data=json.dumps({}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()