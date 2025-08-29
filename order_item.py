from order import Order


class Order_Item(Order):
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity