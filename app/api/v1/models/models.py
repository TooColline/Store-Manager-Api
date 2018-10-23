'''This module holds all data and logic of the application'''
from datetime import datetime
users = []
Products = []
salerec = []

class UserModel():
    '''Initializes a new user'''
    def __init__(self, email, password, role):
        self.id = len(users) + 1
        self.email = email
        self.password = password
        self.role = role

    def save(self):
        '''Saves a user by appending them to the users list'''
        new_user = {
                "id": self.id,
                "email": self.email,
                "password": self.password,
                "role": self.role
            }
        users.append(new_user)

    def getEmail(self):
        return self.email


class ProductsModel():
    '''Initializes a new product'''
    def __init__(self, data):
        self.id = len(Products) + 1
        self.product = data

    def save(self):
        '''Saves a product by appending it to the products list'''
        new_product = {
            "product_id": self.id,
            "name": self.product["name"],
            "price": self.product["price"],
            "category": self.product["category"],
            'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        Products.append(new_product)


class SalesModel():
    '''Initializes a sale'''

    def __init__(self, data):
        self.id = len(salerec) + 1
        self.sales = data

    '''Saves a sale to sale records'''
    def save(self):
        new_sale = {
                    "sale_id": self.sales["sale_id"],
                    "name": self.sales["name"],
                    "price": self.sales["price"],
                    "quantity": self.sales["quantity"],
                    "totalamt": self.sales["totalamt"]
                    }
        salerec.append(new_sale)

def destroy():
    '''Destroys all the data logic of the application during taredown'''
    users.clear()
    Products.clear()
    salerec.clear()