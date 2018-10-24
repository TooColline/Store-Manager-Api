'''This module holds all data and logic of the sales in the application'''
from flask import jsonify
from datetime import datetime

salerec = []

class SalesModel():
    '''Initializes a sale'''

    def __init__(self, name, price, quantity, totalamt):
        self.id = len(salerec) + 1
        self.name = name
        self.price = price
        self.quantity = quantity
        self.totalamt = totalamt

    '''Saves a sale to sale records'''
    def save(self):
        new_sale = {
            "sale_id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "totalamt": (self.price * self.quantity)
            }
        salerec.append(new_sale)

        return new_sale