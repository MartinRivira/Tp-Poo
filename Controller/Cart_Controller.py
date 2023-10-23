from service.Cart_Service import CartService

class CartController:
    def __init__(self):
        self.cart_service = CartService()

    def add_product(self, product):
        self.cart_service.add_product(product)  

    def calculate_total_cost(self):
        return self.cart_service.calculate_total_cost()

