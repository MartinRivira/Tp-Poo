from controller.cart_controller import CartController
from models.product import Product
from models.cart import Cart
from models.Discount_Handler import DiscountHandler
from models.supermarket import Supermarket


if __name__ == "__main__":
    leche = Product("leche", 340)
    sandia = Product("sandia", 1174)
    oreo = Product("oreo", 423)
    

    cart_controller = CartController()
    cart_controller.add_product(leche)
    cart_controller.add_product(sandia)
    cart_controller.add_product(oreo)
    


    total_cost = cart_controller.calculate_total_cost()

    print(f"Total cost: ${total_cost}")
