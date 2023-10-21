from Controller.Cart_Controller import CartController
from service.Cart_Service import CartService
from models.Product import Product

if __name__ == "__main__":
    leche = Product("leche", 2.0)
    sandia = Product("sandia", 6.0)
    oreo = Product("oreo", 1.0)

    cart = Cart()
    cart.add_item(leche)
    cart.add_item(sandia)
    cart.add_item(oreo)

    leche_handler = DiscountHandler()
    sandia_handler = DiscountHandler()
    leche_handler.next_handler = sandia_handler

    cart_controller = CartController()
    discounted_total = cart_controller.apply_discount(cart, leche_handler)

    cart_service = CartService()
    cart_service.checkout(cart)

    print(f"Total con descuento: ${discounted_total}")
