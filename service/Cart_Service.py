from models.cart import Cart

class CartService:
    def __init__(self):
        self.cart = Cart()

    def add_item(self, product):
        self.cart.add_item(product)

    def calculate_total_cost(self):
        return self.cart.calculate_total_cost()
