import unittest
from flask import json
from app import app # Modify <filelname> if required in future: from <filename> import app

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
    
    # Test Case to verify health endpoint 
    def test_healthcheck_endpoint_success(self):
        response = self.app.get('/health')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')


    # Test Case to verify health endpoint 
    def test_healthcheck_endpoint_failure(self):      
        app.application_status = "failure"
        response = self.app.get('/health')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code,500)
        self.assertEqual(data['status'], 'failure')
        
    
    # Cleanup if required
    def tearDown(self):
        #Cleanup if required
        pass

if __name__ == '__main__':
    unittest.main()