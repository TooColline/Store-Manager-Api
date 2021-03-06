import os
from flask import Flask, jsonify, request, abort, make_response
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from functools import wraps
import jwt

from . import general_helper_functions
from ..models import ProductsModel, SalesModel
from ..utils import token_verification

class AddProduct(Resource):
    """Simple class that holds admin endpoints"""

    def post(self):
        """POST /products"""

        logged_user = token_verification.verify_tokens()
        general_helper_functions.abort_user_if_not_admin(logged_user)
                  
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
                message="Bad request. The price should be a positive number and not 0."
            ), 400))

        if not isinstance(name, str):
            abort(make_response(jsonify(
                message="Bad request. The product name should be in a string format."
            ), 400))

        if not isinstance(category, str):
            abort(make_response(jsonify(
                message="Bad request. The category should be in a string format"
            ), 400))

        if ProductsModel.Products:
            """Checking if product is in the store already"""
            try:
                """Those with similar name"""
                already_existing_product = [
                    product for product in ProductsModel.Products if product['name'] == name][0]

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

class GetAllSales(Resource):
    """A simple class that keeps track of sales records"""

    def get(self):
        """For GET /saleorder"""

        token_verification.verify_tokens()
        
        if not SalesModel.salerec:
            # Check if there is no sale records made yet

            abort(make_response(
                jsonify(message="There are no sale orders made yet"), 404))

        # Confirm if at least one sale record exists
        response = jsonify({
            'message': "Successfully fetched all the sale orders",
            'sale_orders': SalesModel.salerec
            })
        response.status_code = 200
        return response