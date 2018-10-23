from flask import abort, jsonify, make_response
from datetime import datetime

from ..models import models
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
        product_id = len(models.Products) + 1
        product = {
            'product_id': product_id,
            'name': name,
            'price': price,
            'category': category,
        }

        models.Products.append(product)
        response = jsonify({
            "message": "Product added to store successfully",
            "product": models.Products[-1]})
        response.status_code = 201
    else:
        """no parameters missing"""
        miss_parameter_required()
    return response

def get_specific_product(product_id):
    """General method to get a specific product from the store"""

    specific_product = None

    for product in models.Products:
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
        sale_id = len(models.salerec) + 1
        SaleOrder = {
            'sale_id': sale_id,
            'name': name,
            'price': price,
            'quantity': quantity,
            'totalamt': totalamt,
            'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        models.salerec.append(SaleOrder)
        response = jsonify({
            "message": "Sale record has been created successfully",
            "SaleOrder": models.salerec[-1]})
        response.status_code = 201
    else:
        # if any of the required parameters is missing or none
        miss_parameter_required()
    return response

def get_specific_sale_record(sale_id):
    """Get specific record given a sale id"""
    specific_sale_record = None
    for sale_order in models.salerec:
        if sale_order['sale_id'] == sale_id:
            specific_sale_record = sale_order
            break
    if not specific_sale_record:
        abort_if_not_found(sale_id)
    return specific_sale_record