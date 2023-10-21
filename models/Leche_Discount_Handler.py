from models.Discount_Handler import DiscountHandler


class LecheDiscountHandler(AbstractDiscountHandler):
    def apply_discount(self, cart):
        # Aplicar descuento en productos lácteos
        discount = 0.1  # 10% de descuento en productos lácteos
        if self.next_handler is not None:
            return self.next_handler.apply_discount(cart) - (discount * cart.get_dairy_cost())
        return cart.get_dairy_cost()

