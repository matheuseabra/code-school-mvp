
import json
import unittest

from project import db
from project.api.models import User
from project.tests.base import BaseTestCase


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_users(self):
        """Test that the /ping route behaves correctly."""
        response = self.client.get('users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('PONG', data["message"])
        self.assertIn('success', data["status"])

    def test_create_user(self):
        """Test creating a user"""
        with self.client:
            response = self.client.post('/users', data=json.dumps({'username': 'Bob', 'email': 'bob@email.com'}), content_type='application/json') # noqa
            data = json.loads(response.data.decode())
            self.assertEqual('bob@email.com was added!', data['message'])
            self.assertIn('success', data['status'])

    def test_create_user_invalid_json(self):
        """Test an error is thrown if the JSON object is empty"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({}),
                content_type='application/json'
                )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

    def test_create_user_invalid_json_keys(self):
        """Test an error is thrown if the JSON object does not have a username key""" # noqa
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({'email': 'test@email.org'}),
                content_type='application/json'
                )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

    def test_create_user_duplicate_email(self):
        """Test an error is thrown if the email already exists"""
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'michael',
                    'email': 'michael@mherman.org'
                }),
                content_type='application/json'
                )
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'michael',
                    'email': 'michael@mherman.org'
                }),
                content_type='application/json'
                )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Sorry, that email already exists', data['message']) # noqa
            self.assertIn('Fail', data['status'])

    def test_single_user(self):
        """Test it returns a single user"""
        user = add_user('test', 'test@email.com')
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('bob', data['data']['username'])
            self.assertIn('bob@email.com', data['data']['email'])
            self.assertIn('success', data['status'])

    def test_single_user_no_id(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client:
            response = self.client.get('users/xxx')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user_incorrect_id(self):
        """Ensure error is thrown if an id is incorrect."""
        with self.client:
            response = self.client.get('users/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_all_users(self):
        """Ensure all users are returned"""
        add_user('matt', 'matt@email.com')
        add_user('bob', 'bob@email.com')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
