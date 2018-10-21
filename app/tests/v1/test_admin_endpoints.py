import json
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
    
    def test_get_sale_records(self):
        """For Test GET /saleorder only if a sale record exists"""

        self.app_test_client.post(
        '{}/saleorder'.format(
            self.base_url), data=json.dumps(dict(
                                                sale_id = 1,
                                                name = "Sample Bags",
                                                price = 20,
                                                quantity = 1,
                                                totalamt = 20
                                                )), content_type='application/json')

        response = self.app_test_client.get(
            '{}/saleorder'.format(self.base_url)
        )
        
        self.assertEqual(response.status_code, 200)

        self.assertEqual(general_helper_functions.convert_json(
            response)['SaleOrder'][0]['name'], "Sample Bags")
    def test_add_new_product_price_negative(self):
        """Test POST /products with the price of a negative number or zero"""

        response = self.app_test_client.post('{}/products'.format(
            self.base_url), json={
                'product_id': 1, 'name': "Hand Bag", 'price': 0, 'category':'Clothing'
                }, headers={'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 400)

        self.assertEqual(general_helper_functions.convert_json(
            response)['message'],
            'Bad request. The price should be a positive number and not 0.')

    def test_add_new_product_name_not_string(self):
        """Test POST /products with a product name different from string"""

        response = self.app_test_client.post('{}/products'.format(
            self.base_url), json={
                'product_id': 1, 'name': 2, 'price': 200, 'category':'Accessories'
                }, headers={'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 400)

        self.assertEqual(general_helper_functions.convert_json(
            response)['message'],
            'Bad request. The product name should be in a string format.')
    
    def test_add_new_product_category_not_string(self):
        """Test POST /products with the category not in a string format"""

        response = self.app_test_client.post('{}/products'.format(
            self.base_url), json={
                'product_id': 1, 'name': "Shoes", 'price': 1000, 'category': 15
                }, headers={'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 400)

        self.assertEqual(general_helper_functions.convert_json(
            response)['message'],
            'Bad request. The category should be in a string format')

    def test_add_new_product_product_already_existing_in_store(self):
        """Test POST /products with a product name that already exists"""

        self.app_test_client.post('{}/products'.format(
            self.base_url), json={
                'product_id': 1, 'name': 'Hand Bag', 'price': 1500, 'category': 'Clothing'
                }, headers={'Content-Type': 'application/json'})

        response = self.app_test_client.post('{}/products'.format(
            self.base_url), json={
                'product_id': 1, 'name': "Hand Bag", 'price': 1500, 'category': "Clothing"
                }, headers={'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 400)

        self.assertEqual(general_helper_functions.convert_json(
            response)['message'],
            'Sorry. A product with a similar name already exists.')
