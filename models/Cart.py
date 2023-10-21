from models.Cart import Cart
from models.Product import Product


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def calculate_total_cost(self):
        return sum(item.price for item in self.items)

