import os
import pickle


class Saver:

    def __init__(self, product, user, order):
        self.product = product
        self.user = user
        self.order = order

    def __str__(self):
        return f"[{self.product}] {self.user} - {self.order}"
    
    @staticmethod
    def save(file_name, obj_list):
        with open(file_name, "wb") as f:
            pickle.dump(obj_list, f)

    @classmethod
    def save_users(cls, users_list):
        cls.save('users.pkl', users_list)

    @classmethod
    def save_products(cls, products_list):
        cls.save('products.pkl', products_list)

    @classmethod
    def save_orders(cls, orders_list):
        cls.save('orders.pkl', orders_list)

class Loader:

    def __init__(self, product, user, order):
        self.product = product
        self.user = user
        self.order = order
        
    @staticmethod
    def open_file(file_name: str) -> list:
        if os.path.exists(file_name):
            with open(file_name, "rb") as f:
                my_obj_list = pickle.load(f)
            
            return my_obj_list
        else:
            return []

    @classmethod
    def load_users(cls):
        return cls.open_file('users.pkl')
    
    @classmethod
    def load_products(cls):
        return cls.open_file('products.pkl')
    
    @classmethod
    def load_orders(cls):
        return cls.open_file('orders.pkl')

        
                
if __name__ == "__main__":
    class MyClass:

        def __init__(self, value):
            self.value = value
        def print_value(self):
            print(self.value)

    obj_list = [MyClass(1), MyClass(2)]
    
    Saver.save_users(obj_list)
    objs = Loader.load_users()
    for obj in objs:
        obj.print_value()
        
    objs = Loader.load_products()
    print(objs)