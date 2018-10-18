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