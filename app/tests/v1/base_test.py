import unittest

from app import create_app
from instance.config import config
 
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

if __name__ == '__main__':
    unittest.main()