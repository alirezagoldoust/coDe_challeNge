from order import Order
from order_item import Order_Item

class Customer:
    id = 0
    def __init__(self, username, orders, basket):
        self.__id = Customer.id
        self.name = username
        self.orders = orders
        self.basket = basket
        Order.id += 1

    def get_products(Product):
        return Product.get_products()


    def select_product(self):
        products = self.get_products()
        product_id = int(input("Enter product id: "))
        product = products[product_id]
        return product

    def get_quantity(self):
        count = int(input("Enter quantity: "))
        return count

    def add_to_basket(self):
        product = self.select_product()
        count = self.get_quantity()
        new_order_item = Order_Item(product, count)
        if count < product.stock:
            self.basket.append(new_order_item)
        else:
            print("unavailable!")