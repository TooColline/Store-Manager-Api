from flask import abort, jsonify, make_response
from datetime import datetime

from ..models import products

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
        product_id = len(products.Products) + 1
        product = {
            'product_id': product_id,
            'name': name,
            'price': price,
            'category': category,
            'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        products.Products.append(product)
        response = jsonify({
            "message": "Product added to store successfully",
            "product": products.Products[-1]})
        response.status_code = 201
    else:
        """no parameters missing"""
        miss_parameter_required()
    return response