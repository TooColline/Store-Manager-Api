from flask import Flask, jsonify, request, abort, make_response
from flask_restful import Resource

from . import general_helper_functions
from ..models import products

class Admin(Resource):
    """Simple class that holds admin endpoints"""

    def post(self):
        """POST /products"""
                  
        data = request.get_json()
        general_helper_functions.json_null_request(data)
        
        try:
            name = data['name']
            price = data['price']
            category = data['category']

        except KeyError:
            general_helper_functions.miss_parameter_required()

        if price < 1:
            abort(make_response(jsonify(
                message="Bad request. The price should be a positive number."
            ), 400))

        if not isinstance(name, str):
            abort(make_response(jsonify(
                message="Bad request. The product name should be in a string format."
            ), 400))

        if not isinstance(category, str):
            abort(make_response(jsonify(
                message="Bad request. The category should be in a string format"
            ), 400))

        if products.Products:
            """Checking if product is in the store already"""
            try:
                """Those with similar name"""
                already_existing_product = [
                    product for product in products.Products if product['name'] == name][0]

                abort(make_response(jsonify({
                    "message": "Sorry. A product with a similar name already exists.",
                    "product": already_existing_product}), 400))

            except IndexError:
                """Those with different name"""
                response = general_helper_functions.add_new_product(name, price, category)
        else:
            """Check if there are no products in the store at all"""
            response = general_helper_functions.add_new_product(name, price, category)

        return response