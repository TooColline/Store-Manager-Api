'''This module holds all data and logic of the sales in the application'''

from datetime import datetime

salerec = []

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