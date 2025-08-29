class Order:
    id = 0

    def __init__(self, customer_id, basket, total_price = 0):
        self.__id = Order.id
        self.customer_id = customer_id
        self.basket = basket
        self.total_price = total_price
        Order.id += 1

    def set_total_price(self, basket):
        for order_item in basket:
            self.total_price += (order_item.price * order_item.quantity)