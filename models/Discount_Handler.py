class DiscountHandler:
    def __init__(self, discount):
        self.discount = discount
        self.next_handler = None

    def apply_discount(self, cart):
        total_cost = cart.calculate_total_cost()
        if self.next_handler is not None:
            discounted_cost = self.next_handler.apply_discount(cart)
            # Aplicar descuento adicional según el manejador actual
            return discounted_cost - (self.get_discount() * total_cost)
        return total_cost - (self.discount * total_cost)

    def get_discount(self):
        return self.discount

# Luego, puedes crear subclases de DiscountHandler con descuentos específicos
class LecheDiscountHandler(DiscountHandler):
    def __init__(self):
        super().__init__(0.1)  # 10% de descuento

class SandiaDiscountHandler(DiscountHandler):
    def __init__(self):
        super().__init__(0.05)  # 5% de descuento
