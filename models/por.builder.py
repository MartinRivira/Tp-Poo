class Product:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.discount = discount

    def get_discounted_price(self):
        return self.price * (1 - self.discount)

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Discount: {self.discount * 100}%"

class ProductBuilder:
    def __init__(self):
        self.product = Product("", 0, 0)  

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

# Ejemplo de uso del Builder
builder = ProductBuilder()
leche = builder.set_name("Leche").set_price(340).set_discount(0.1).build()
sandia = builder.set_name("Sandia").set_price(1174).set_discount(0.05).build()

print(leche)
print(sandia)
