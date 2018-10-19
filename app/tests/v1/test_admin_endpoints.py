from . import base_test
from . import general_helper_functions

class TestAdminEndpoints(base_test.BaseTestClass):
    """Tests admin specific endpoints"""

    def test_add_new_product(self):
        """Test POST /products request"""

        response = self.app_test_client.post('{}/products'.format(
            self.base_url), json=self.Product, headers={
                'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 201)

        self.assertEqual(general_helper_functions.convert_json(
            response)['product']['product_id'], 1)

        self.assertEqual(general_helper_functions.convert_json(
            response)['product']['name'], self.Product['name'])

        self.assertEqual(general_helper_functions.convert_json(
            response)['product']['price'], 17000)

        self.assertEqual(general_helper_functions.convert_json(
            response)['product']['category'], self.Product['category'])

        self.assertEqual(general_helper_functions.convert_json(
            response)['message'], 'Product added to store successfully')
    
    def test_get_all_products(self):
        """For GET /products only if it exists"""

        response = self.app_test_client.get(
            '{}/products'.format(self.base_url))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(general_helper_functions.convert_json(
            response)['products'][0]['name'], self.Product['name'])
        
    def test_get_specific_product(self):
        """For GET /products/id only if it exist"""
            
        response = self.app_test_client.get(
            '{}/products/1'.format(self.base_url))

        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(general_helper_functions.convert_json(
            response)['name'], self.Product['name'])