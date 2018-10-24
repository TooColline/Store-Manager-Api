import os
import datetime
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

from flask import Flask, jsonify, request, make_response
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity
)

from instance import config
from ..utils.user_validator import UserValidator
from ..models import UserModel

class SignUp(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({
                                    "message": "Missing critical credentials"
                                    }), 400)
        email = data["email"]
        password = generate_password_hash(data["password"], method='sha256')
        role = data["role"]
        UserValidator.validate_user_info(self, data)
        user = UserModel.UserModels(email, password, role)
        res = user.save()
        return make_response(res, 202)


class Login(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({
                "message": "Kindly input your information"
            }
            ), 400)
        email = data["email"]
        password = data["password"]

        for user in UserModel.users:
            if email == user["email"] and check_password_hash(user["password"], password):
                token = jwt.encode({
                    "email": email,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta
                                  (minutes=30)
                }, os.getenv('JWT_SECRET_KEY', default='thisissecret'))
                return make_response(jsonify({
                             "message": "You are successfully logged in",
						     "token": token.decode("UTF-8")}), 200)
        return make_response(jsonify({
            "message": "Wrong credentials entered"
        }
        ), 403)
