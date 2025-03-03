#!/usr/bin/python3
"""Unit tests for User API endpoints"""

import unittest
import json
from hbnb.app import create_app

class TestUserEndpoints(unittest.TestCase):
    """Test cases for User endpoints"""

    def setUp(self):
        """Set up test client"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.test_user = {"email": "test@example.com", "password": "securepass"}

    def test_get_all_users(self):
        """Test GET /api/v1/users"""
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        """Test POST /api/v1/users with valid data"""
        response = self.client.post('/api/v1/users/',
                                    data=json.dumps(self.test_user),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid(self):
        """Test POST /api/v1/users with missing email"""
        response = self.client.post('/api/v1/users/',
                                    data=json.dumps({"password": "securepass"}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()