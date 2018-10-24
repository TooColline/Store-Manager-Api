from flask import jsonify, abort, make_response
from flask_restful import Resource

from . import general_helper_functions
from ..models import ProductsModel, SalesModel
from ..utils import token_verification

class AdminAndStoreAttendant(Resource):
    """Simple class that holds functions for both admin and store attendant"""

    def get(self):
        """For GET /products"""
        if not ProductsModel.Products:
            # If no products exist in the store yet
            abort(make_response(
                jsonify(message="There are no products in the store yet"), 404))

        # Check if there is at least one product in the store
        response = jsonify({
            'message': "Successfully fetched all the products",
            'products': ProductsModel.Products
            })
        response.status_code = 200

        return response
    
class GetSpecificProduct(Resource):
    """Simple class that hold functions to get a specific product"""
    
    def get(self, product_id):
        """For GET /products/<int:product_id>"""

        token_verification.verify_tokens()

        for product in ProductsModel.Products:
            if product["product_id"] == product_id:
                return make_response(jsonify({
                    "message": "{} retrieved successfully".format(product["name"]),
                    "product": product
                }
                ), 200)

            else:
                return make_response(jsonify({
                    "message": "Product with id {} not found".format(product_id)
                }
                ), 404)