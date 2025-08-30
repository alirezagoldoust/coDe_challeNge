from product_management import Product_management
from user_management import User_management


def seller_menu(user_manager: User_management):
    product_manager = Product_management()

    while True:
        print("1. Add Product")
        print("2. Show My Products")
        print("3. Exit")
        print()

        user_input = input("Enter your choice: ")

        match user_input :
            case "1" :
                print("enter product name: ")
                product_name = input()
                print("enter product price: ")
                product_price = input()
                print("enter product stock: ")
                product_stock = input()

                product_manager.add_products(product_name , product_price, product_stock,
                                             user_manager.current_user.username)

            case "2" :
                products = product_manager.get_product_list()
                for product in products :
                    if product.seller_username == user_manager.current_user.username :
                        print(product)
                print()

            case "3" :
                exit()


def customer_menu(user_manager: User_management):
    user_name = user_manager.current_user.username
    customer_list = user_manager.customers_list
    product_manager = Product_management()

    customer = next((c for c in customer_list if c.username == user_name), None)

    while True:
        print("1. Add Product to my basket")
        print("2. Show All Products")
        print("3. Place Order")
        print("4. Exit")
        print()

        user_input = input("Enter your choice: ")

        match user_input :

            case "1" :
                product_name = input("Enter product name: ")
                product_count = int(input("Enter product count: "))
                products = product_manager.get_product_list()

                for product in products :
                    if product.name == product_name :
                        customer.add_to_basket(product, product_count)

            case "2" :
                products = product_manager.get_product_list()
                for product in products :
                    print(product)
                print()

            case "3" :
                customer.basket.clear()

            case "4":
                exit()
    

def main():
    user_manager = User_management()
    print("Wellcome to digikala")

    input_username = input("Please enter your username: ")
    user_manager.login_user(username=input_username)

    while not user_manager.current_user:
       try:
            user_role = user_manager.current_user.get_role()
       except:
           user_role = None

       user_role = input("Please enter your role: ")
       if user_role == "Seller":
           role = "Seller"
       elif user_role == "Customer":
           role = "Customer"

       user_manager.sing_up_user(input_username, role)

       user_manager.login_user(username=input_username)

    print(f"\nWelcome, {user_manager.current_user.get_username()}!")

    user_role = user_manager.current_user.get_role()

    if user_role == "Seller":
        seller_menu(user_manager)

    elif user_role == "Customer":
        customer_menu(user_manager)


if __name__ == "__main__":
    main()