from . import base_test
from . import general_helper_functions

class AdminStoreAttendant(base_test.BaseTestClass):
    """Simple class that holds test functions for both admin and store attendant"""

    def test_get_all_products(self):
        """For GET /products only if it exists"""

        response = self.app_test_client.get(
            '{}/products'.format(self.base_url))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(general_helper_functions.convert_json(
            response)['products']), 0)
