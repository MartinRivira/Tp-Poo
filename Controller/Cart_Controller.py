from service.Cart_Service import CartService

class CartController:
    def __init__(self):
        self.cart = CartService()
        self.discount_handler = None

    def add_product(self, product):
        self.cart.add_item(product)

    def apply_discount_handler(self, discount_handler):
        self.discount_handler = discount_handler

    def calculate_total_cost(self):
        if self.discount_handler:
            return self.discount_handler.apply_discount(self.cart)
        else:
            return self.cart.calculate_total_cost()
