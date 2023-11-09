from domain.cart import Cart

class CartService:
    def __init__(self):
        self.cart = Cart()

    def add_product(self, product):
        self.cart.add_item(product)

    def calculate_total_cost(self):
        return self.cart.calculate_total_cost()

    def apply_discount(self, discount_handler):
        
        pass
