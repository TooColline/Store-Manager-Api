from flask import Flask, jsonify, request, abort, make_response
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from . import general_helper_functions
from ..models import ProductsModel, SalesModel
from ..utils import token_verification

class StoreAttendant(Resource):
    """Simple class that holds the store endpoints"""

    def post(self):
        """POST /products"""

        token_verification.verify_tokens()
                  
        data = request.get_json()
        general_helper_functions.json_null_request(data)
        
        try:
            name = data['name']
            price = data['price']
            quantity = data['quantity']
            totalamt = data['totalamt']

        except KeyError:
            general_helper_functions.miss_parameter_required()

        if not isinstance(name, str):
            abort(make_response(jsonify(
                message="Bad request. The product name should be a string."
            ), 400))
        
        if not isinstance(price, int):
            abort(make_response(jsonify(
                message="Bad request. The product price should be an integer."
            ), 400))
        
        if price < 1:
            abort(make_response(jsonify(
                message="Bad request. The product price should be a positive number above 0."
            ), 400))

        if not isinstance(quantity, int):
            abort(make_response(jsonify(
                message="Bad request. The quantity should be an integer."
            ), 400))

        sale_order = SalesModel.SalesModel(name, price, quantity, totalamt)
        response = sale_order.save()

        return make_response(jsonify({
            "message": "Checkout complete",
            "saleorder": response
        }), 201)

class SpecificSaleRecord(Resource):

    def get(self, sale_id):
        """GET /saleorder/<int:sale_order_id>"""
        sale_order = general_helper_functions.get_specific_sale_record(sale_id)
        response = jsonify(sale_order)
        response.status_code = 200