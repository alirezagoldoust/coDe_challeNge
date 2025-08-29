from file_management import Saver, Loader

class Product_management :
    def __init__(self) :
        self.products_list = Loader.load_products()

    def add_products(self , name , price , stock, seller_username):
        new_product = Product(name , price , stock, seller_username)
        self.products_list.append(new_product)
        Saver.save_products(self.products_list)
    
    def get_product_list(self) :
        return self.products_list
    

class Product : 
    number_of_products = 0

    def __init__(self , name , price , stock, seller_username):
        self.name = name
        self.price = price
        self.stock = stock
        self.seller_username = seller_username
        self.id = Product.number_of_products
        Product.number_of_products += 1