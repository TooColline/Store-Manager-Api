from flask import abort, jsonify, make_response
from datetime import datetime

from ..models import products, sales

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

def get_specific_product(product_id):
    """General method to get a specific product from the store"""

    specific_product = None

    for product in products.Products:
        if product['product_id'] == product_id:
            specific_product = product
            break

    if not specific_product:
        abort_if_not_found(product_id)

    return specific_product

def abort_if_not_found(product_id):
    """General method to abort get request if the specific product is not in store"""

    abort(make_response(jsonify(
        message="Product with id number {} not found".format(product_id)), 404))

def add_sale_record(name, price, quantity, totalamt):

    """Creates a new sale record"""

    if name and price and quantity and totalamt:
        # If all the required data are provided
        sale_id = len(sales.salerec) + 1
        SaleOrder = {
            'sale_id': sale_id,
            'name': name,
            'price': price,
            'quantity': quantity,
            'totalamt': totalamt,
            'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        sales.salerec.append(SaleOrder)
        response = jsonify({
            "message": "Sale record has been created successfully",
            "SaleOrder": sales.salerec[-1]})
        response.status_code = 201
    else:
        # if any of the required parameters is missing or none
        miss_parameter_required()
    return response