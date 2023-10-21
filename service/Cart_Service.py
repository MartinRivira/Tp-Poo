from models.Supermarket import Supermarket

class CartService:
    def __init__(self):
        pass

    def checkout(self, cart):
        supermarket = Supermarket()
        supermarket.checkout(cart)
