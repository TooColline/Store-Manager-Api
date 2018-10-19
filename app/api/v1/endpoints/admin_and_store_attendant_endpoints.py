from flask import jsonify, abort, make_response
from flask_restful import Resource

from . import general_helper_functions
from ..models import products

class AdminAndStoreAttendant(Resource):
    """Simple class that holds functions for both admin and store attendant"""

    def get(self):
        """For GET /products"""
        if not products.Products:
            # If no products exist in the store yet
            abort(make_response(
                jsonify(message="There are no products in the store yet"), 404))

        # Check if there is at least one product in the store
        response = jsonify({'products': products.Products})

        response.status_code = 200

        return response