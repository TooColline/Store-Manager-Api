from . import base_test
from . import general_helper_functions

class TestStoreAttendantEndpoints(base_test.BaseTestClass):
    """Tests admin specific endpoints"""

    def test_add_new_sale(self):
        """For POST /saleorder request"""

        response = self.app_test_client.post('{}/saleorder'.format(
            self.base_url), json=self.SaleOrder, headers={
                'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 201)

        self.assertEqual(general_helper_functions.convert_json(
            response)['SaleOrder']['name'], self.SaleOrder['name'])

        self.assertEqual(general_helper_functions.convert_json(
            response)['SaleOrder']['price'], self.SaleOrder['price'])

        self.assertEqual(general_helper_functions.convert_json(
            response)['SaleOrder']['quantity'], self.SaleOrder['quantity'])

        self.assertEqual(general_helper_functions.convert_json(
            response)['SaleOrder']['totalamt'], self.SaleOrder['totalamt'])

        self.assertEqual(general_helper_functions.convert_json(
            response)['message'], 'Sale record has been created successfully')
