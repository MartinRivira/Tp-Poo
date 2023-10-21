from models.Discount_Handler import DiscountHandler

class SandiaDiscountHandler(AbstractDiscountHandler):
    def apply_discount(self, cart):
        # Aplicar descuento en productos frescos
        discount = 0.05  # 5% de descuento en productos frescos
        if self.next_handler is not None:
            return self.next_handler.apply_discount(cart) - (discount * cart.get_fresh_cost())
        return cart.get_fresh_cost()

