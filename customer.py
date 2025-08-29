from order import Order
from order_item import Order_Item
from product_management import Product_management


class Customer():
    id = 0

    def __init__(self, username, orders = None,):
        self.__id = Customer.id
        self.username = username
        self.orders = orders
        self.basket = []
        Order.id += 1

    @staticmethod
    def get_products():
        return Product_management.get_product_list()

    def get_quantity(self):
        count = int(input("Enter quantity: "))
        return count

    def add_to_basket(self, product, count = 1):
        new_order_item = Order_Item(product, count)
        
        if int(count) < int(product.stock):
            self.basket.append(new_order_item)
        elif int(count) > 10:
            print("Sorry, you can't buy more than 10 products.")
        else:
            print("unavailable!")