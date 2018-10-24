import unittest

from app import create_app
from instance.config import config
from . import general_helper_functions
 
class BaseTestClass(unittest.TestCase):
 
    def setUp(self):
        """set up application for testing"""
        
        self.app = create_app('testing')
        self.base_url = 'api/v1'
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app_test_client = self.app.test_client()
        self.app.testing = True

        self.Product = {
        'name': 'Carpet',
        'price': 17000,
        'category': 'Home & Furniture'
        }

        self.SaleOrder = {
            'name': 'Carpet',
            'price': 17000,
            'quantity': 2,
            'totalamt': (17000 * 2)
        }
        
    def tearDown(self):
        """tear down dictionaries"""
        self.app_context.pop()

    def register_admin_test_account(self):
        """Registers an admin user test account"""
            
        resp = self.app_test_client.post("api/v1/auth/signup",
        json={
        "email": "admin@gmail.com",
        "role": "Admin",
        "password": "Password2@"
        }, 
        headers={
        "Content-Type": "application/json"
        })

        return resp
    
    def login_admin_test(self):
        """Verify's the admin test account"""

        res = self.app_test_client.post("api/v1/auth/login",
        json={
            "email": "admin@gmail.com",
            "password": "Password2@"
        },
        headers={
        "Content-Type": "application/json"
        })

        auth_token = general_helper_functions.convert_json(
        res)['token']

        return auth_token

if __name__ == '__main__':
    unittest.main()