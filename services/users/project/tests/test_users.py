
import json
import unittest

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_users(self):
        """Test that the /ping route behaves correctly."""
        response = self.client.get('users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data["message"])
        self.assertIn('success', data["status"])

    def test_create_user(self):
        """Test creating a user"""
        with self.client:
            response = self.client.post('/users', data=json.dumps({'username': 'Bob', 'email': 'bob@email.com'}), content_type='application/json') # noqa
            data = json.loads(response.data.decode())
            self.assertEqual('bob@email.com was added!', data['message'])
            self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
