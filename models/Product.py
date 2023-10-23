from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_discount(self):
        pass

class Product(AbstractProduct):
    def get_discount(self):
        return 0
