from controller.cart_controller import CartController
from domain.product import Product
from domain.Discount_Handler import LecheDiscountHandler, SandiaDiscountHandler, OreoDiscountHandler
from service.Cart_Service import CartService

if __name__ == "__main__":
    leche = Product("leche", 340)
    sandia = Product("sandia", 1174)
    oreo = Product("oreo", 423)
    panintegral = Product("panintegral", 500)

    cart_service = CartService()
    cart_service.add_product(leche)
    cart_service.add_product(sandia)
    cart_service.add_product(oreo)
    cart_service.add_product(panintegral)

    leche_discount = LecheDiscountHandler()
    sandia_discount = SandiaDiscountHandler()
    oreo_discount = OreoDiscountHandler()

    leche_discount.next_handler = sandia_discount
    cart_service.apply_discount(leche_discount)

    total_cost = cart_service.calculate_total_cost()

    print(f"Total cost: ${total_cost}")