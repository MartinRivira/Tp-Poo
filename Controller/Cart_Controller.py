from models.Discount_Handler import DiscountHandler
from models.Cart import Cart
from Controller.Cart_Controller import CartController

class CartController:
    def __init__(self):
        pass

    def apply_discount(self, cart, discount_handler):
        discounted_total = discount_handler.apply_discount(cart)
        return discounted_total
