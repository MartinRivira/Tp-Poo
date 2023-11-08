class Supermarket:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Supermarket, cls).__new__(cls)
        return cls._instance

    def checkout(self, cart):
        pass
