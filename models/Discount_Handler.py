from abc import ABC, abstractmethod

class AbstractDiscountHandler(ABC):
    def __init__(self):
        self.next_handler = None

    @abstractmethod
    def apply_discount(self, cart):
        pass
