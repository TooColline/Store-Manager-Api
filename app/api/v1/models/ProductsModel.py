'''This module holds all data and logic of the products in the application'''

from datetime import datetime

Products = []

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