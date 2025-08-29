class Product_management :
    def __init__(self) :
        self.products_list = []

    def add_products(self , name , price , stock, seller_username):
        new_product = Product(name , price , stock, seller_username)
        self.products_list.append(new_product)




class Product : 
    number_of_products = 0

    def __init__(self , name , price , stock, seller_username):
        self.name = name
        self.price = price
        self.stock = stock
        self.seller_username = seller_username
        self.id = Product.number_of_products
        Product.number_of_products += 1