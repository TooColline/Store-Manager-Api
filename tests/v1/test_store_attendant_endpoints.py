from . import base_test
from . import general_helper_functions

class TestStoreAttendantEndpoints(base_test.BaseTestClass):
    """Tests admin specific endpoints"""

    def test_add_new_sale(self):
        """For POST /saleorder request"""
        self.register_admin_test_account()
        token = self.login_admin_test() 

        response = self.app_test_client.post('{}/saleorder'.format(
            self.base_url), json=self.SaleOrder, headers=dict(Authorization=token),
            content_type='application/json')

        self.assertEqual(response.status_code, 201)

        self.assertEqual(general_helper_functions.convert_json(
            response)['saleorder']['name'], self.SaleOrder['name'])

        self.assertEqual(general_helper_functions.convert_json(
            response)['saleorder']['price'], self.SaleOrder['price'])

        self.assertEqual(general_helper_functions.convert_json(
            response)['saleorder']['quantity'], self.SaleOrder['quantity'])

        self.assertEqual(general_helper_functions.convert_json(
            response)['saleorder']['totalamt'], self.SaleOrder['totalamt'])

        self.assertEqual(general_helper_functions.convert_json(
            response)['message'], 'Sale successfully made')
    
    def test_get_specific_sale_record(self):
        """For Test GET /saleorder/id only if at least one sale record exists"""
        
        self.register_admin_test_account()
        token = self.login_admin_test()

        response = self.app_test_client.get(
            '{}/saleorder'.format(self.base_url), json={
            'sale_id': 1,
            'name': "Sample Bags",
            'price': 20,
            'quantity': 1,
            'totalamt': 20
            },
        headers=dict(Authorization=token),
        content_type='application/json')

        response = self.app_test_client.get(
            '{}/saleorder/1'.format(self.base_url),
            headers=dict(Authorization=token),
            content_type='application/json'
            )
            
        self.assertEqual(response.status_code, 200)
    
    def test_add_sale_with_price_below_one(self):
        """Test POST /saleorder with the product price zero or negative"""
        self.register_admin_test_account()
        token = self.login_admin_test()

        response = self.app_test_client.post('{}/saleorder'.format(
            self.base_url), json={'name': 'Torch', 'price': -10, 'quantity': 5, 'totalamt': ""},
            headers=dict(Authorization=token),
            content_type='application/json')

        self.assertEqual(response.status_code, 400)

        self.assertEqual(general_helper_functions.convert_json(
            response)['message'], 'Bad request. The product price should be a positive number above 0.')

    def test_add_sale_with_product_name_not_string(self):
        """Test POST /saleorder with the product name not in a string format"""
        self.register_admin_test_account()
        token = self.login_admin_test()

        response = self.app_test_client.post('{}/saleorder'.format(
            self.base_url), json={'name': 1, 'price': 1500, 'quantity': 10, 'totalamt': ""},
            headers=dict(Authorization=token),
            content_type='application/json')

        self.assertEqual(response.status_code, 400)

        self.assertEqual(general_helper_functions.convert_json(
            response)['message'], 'Bad request. The product name should be a string.')

    def test_add_sale_with_price_not_digit_format(self):
        """Test POST /saleorder with the product price not a valid format"""
        self.register_admin_test_account()
        token = self.login_admin_test()

        response = self.app_test_client.post('{}/saleorder'.format(
            self.base_url), json={'name': "Hand Bag", 'price': "1500", 'quantity': 3, 'totalamt': ""},
            headers=dict(Authorization=token),
            content_type='application/json')

        self.assertEqual(response.status_code, 400)

        self.assertEqual(general_helper_functions.convert_json(
            response)['message'], 'Bad request. The product price should be an integer.')

    def test_add_sale_with_invalid_quantity(self):
        """Test POST /saleorder with an invalid quantity not in digit"""
        self.register_admin_test_account()
        token = self.login_admin_test()
        
        response = self.app_test_client.post('{}/saleorder'.format(
            self.base_url), json={'name': "Hand Bag", 'price': 1500, 'quantity': "5", 'totalamt': ""}, 
            headers=dict(Authorization=token),
            content_type='application/json')

        self.assertEqual(response.status_code, 400)

        self.assertEqual(general_helper_functions.convert_json(
            response)['message'], 'Bad request. The quantity should be an integer.')
