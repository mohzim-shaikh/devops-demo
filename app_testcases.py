import unittest
from flask import json
from app import app  # Modify <filelname> if reqd: from <filename> import app
from unittest.mock import patch


class DevopsDemoAppTests(unittest.TestCase):

    # Initialize Test Client
    def setUp(self):
        self.app = app.test_client()

    # Test Case to verify root endpoint
    def test_hello_world_endpoint(self):
        response = self.app.get('/')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello World')

    # Test Case to verify health-success endpoint
    def test_healthcheck_endpoint_success(self):
        response = self.app.get('/health')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['details'], 'Application is running smoothly')

    # Test Case to verify health-failure endpoint
    @patch('app.application_online', False)
    def test_healthcheck_endpoint_failure(self):
        response = self.app.get('/health')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['status'], 'failure')
        self.assertEqual(data['details'],
                         'Application encountered error')

    # Cleanup if required
    def tearsDown(self):
        # Cleanup if required
        pass


if __name__ == '__main__':
    unittest.main()
