from flask import jsonify, abort, make_response
from flask_restful import Resource

from datetime import datetime
from ..models import UserModel, ProductsModel, SalesModel

def json_null_request(data):
    """Abort, if data has no json object."""
        
    if data is None:
        abort(make_response(jsonify(
            message="Bad request. Request must be in json format"), 400))


def miss_parameter_required():
    """Abort, if data is missing a required parameter."""

    abort(make_response(jsonify(
        message="Bad request. Request missing a required parameter"), 400))


def add_new_product(name, price, category):
    """Creates a new product"""

    if name and price and category:
        """If all product parameters are given"""
        product_id = len(ProductsModel.Products) + 1
        product = {
            'product_id': product_id,
            'name': name,
            'price': price,
            'category': category,
        }

        ProductsModel.Products.append(product)
        response = jsonify({
            "message": "Product added to store successfully",
            "product": ProductsModel.Products[-1]})
        response.status_code = 201
    else:
        """no parameters missing"""
        miss_parameter_required()
    return response

def abort_if_not_found(product_id):
    """General method to abort get request if the specific product is not in store"""

    abort(make_response(jsonify(
        message="Product with id number {} not found".format(product_id)), 404))

def get_specific_sale_record(sale_id):
    """Get specific record given a sale id"""
    specific_sale_record = None
    for sale_order in SalesModel.salerec:
        if sale_order['sale_id'] == sale_id:
            specific_sale_record = sale_order
            break
    if not specific_sale_record:
        abort_if_not_found(sale_id)
    return specific_sale_record

def abort_user_if_not_admin(user):
    user_role = [users['role'] for users in UserModel.users if users['email'] == user][0]
    if user_role!= "Admin":
        abort(make_response(jsonify(
            message="Unauthorized access, please contact your administrator!"
        ), 401))