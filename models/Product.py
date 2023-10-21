from models.Cart import Cart
from models.Product import Product


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discount(self):
        return 0  # Opcional: Implementa un método de descuento específico si es necesario

