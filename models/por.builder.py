from abc import ABC, abstractmethod

class ProductBuilder(ABC):
    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def set_price(self, price):
        pass

    @abstractmethod
    def set_discount(self, discount):
        pass

    @abstractmethod
    def build(self):
        pass

class Product:
    def __init__(self):
        self.name = None
        self.price = None
        self.discount = None

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Discount: {self.discount}"

class ConcreteProductBuilder(ProductBuilder):
    def __init__(self):
        self.product = Product()

    def set_name(self, name):
        self.product.name = name
        return self

    def set_price(self, price):
        self.product.price = price
        return self

    def set_discount(self, discount):
        self.product.discount = discount
        return self

    def build(self):
        return self.product

# Uso del Builder
builder = ConcreteProductBuilder()
leche = builder.set_name("Leche").set_price(340).set_discount(0.1).build()
sandia = builder.set_name("Sandia").set_price(1174).set_discount(0.05).build()

print(leche)
print(sandia)
