'''This module holds all data and logic of the users in the application'''
from flask import make_response, jsonify
from datetime import datetime

users = []


class UserModels():
    '''Initializes a new user'''
    def __init__(self, email, password, role):
        self.id = len(users) + 1
        self.email = email
        self.password = password
        self.role = role

    def getEmail(self):
        return self.email
        
    def save(self):
        '''Saves a user by appending them to the users list'''
        new_user = {
                "id": self.id,
                "email": self.email,
                "password": self.password,
                "role": self.role
            }
        users.append(new_user)

        response = jsonify(new_user)

        return response