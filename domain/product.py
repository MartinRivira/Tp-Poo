from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount = 0.5

    def set_discount(self, discount):
        self.discount = discount

    def get_discounted_price(self):
        return self.price * (1 - self.discount)

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Discount: {self.discount * 100}%"