from abc import ABC, abstractmethod

# Clase abstracta para productos
class AbstractProduct(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_discount(self):
        pass

# Builder
class Product(AbstractProduct):
    def get_discount(self):
        return 0  

# carritos de compras
class AbstractCart(ABC):
    def __init__(self):
        self.items = []

    @abstractmethod
    def add_item(self, product):
        pass

    @abstractmethod
    def calculate_total_cost(self):
        pass

# MVC (carritos de compras)
class Cart(AbstractCart):
    def add_item(self, product):
        self.items.append(product)

    def calculate_total_cost(self):
        return sum(item.price for item in self.items)

# Chain of Responsibility
class AbstractDiscountHandler(ABC):
    def __init__(self):
        self.next_handler = None

    @abstractmethod
    def apply_discount(self, cart):
        pass

# manejo de descuentos
class DiscountHandler(AbstractDiscountHandler):
    def apply_discount(self, cart):
        total_cost = cart.calculate_total_cost()
        if self.next_handler is not None:
            discounted_cost = self.next_handler.apply_discount(cart)
            
            return discounted_cost - (self.get_discount() * total_cost)
        return total_cost - (self.get_discount() * total_cost)

    def get_discount(self):
        return 0.15  # 


class LecheDiscountHandler(DiscountHandler):
    def get_discount(self):
        return 0.1  # 10% de descuento 

class SandiaDiscountHandler(DiscountHandler):
    def get_discount(self):
        return 0.05  # 5% de descuento 


# Singleton
class Supermarket:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Supermarket, cls).__new__(cls)
        return cls._instance

    def checkout(self, cart):

        pass

if __name__ == "__main__":
    # productos
    leche = Product("leche", 2.0)
    sandia = Product("sandia", 6.0)
    oreo = Product("oreo", 1.0)

    # carrito de compras
    cart = Cart()
    cart.add_item(leche)
    cart.add_item(sandia)
    cart.add_item(oreo)

    # cadena de responsabilidad de descuentos 
    leche_handler = DiscountHandler()
    sandia_handler = DiscountHandler()
    
    # cadena estableciendo sandia_handler como el siguiente manejador después de leche_handler
    leche_handler.next_handler = sandia_handler

    # Aplicar descuentos y procesar el carrito
    discounted_total = leche_handler.apply_discount(cart)

    # Realizar el pago en el supermercado (Singleton)
    supermarket = Supermarket()
    supermarket.checkout(cart)


    print(f"Total con descuento: ${discounted_total}")
