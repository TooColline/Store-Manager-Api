from flask import Flask, jsonify, request, abort, make_response
from flask_restful import Resource

from . import general_helper_functions
from app.api.v1.models import products

class AdminAndStoreAttendant(Resource):
    """Simple class that holds functions for both admin and store attendant"""

    def get(self):
        """For GET /products"""

        # Check if there is at least one product in the store
        response = jsonify({'products': products.Products})

        response.status_code = 200
        
        return response
