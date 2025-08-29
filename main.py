from user_management import User_management

def main():
    user_manager = User_management()
    print("Wellcome to digikala")

    input_username = input("Please enter your username: ")
    user_manager.login_user(username=input_username)

    while not user_manager.current_user:
       # input_username = input("The username does not exists, please enter another one...")
       try:
            user_role = user_manager.current_user.get_role()
       except:
           user_role = None
       user_manager.sing_up_user(input_username, user_role)
       # if input_username.lower() == 'exit':
       #     return
       user_manager.login_user(username=input_username)

    print(f"\nWelcome, {user_manager.current_user.get_username()}!")

    user_role = user_manager.current_user.get_role()

    if user_role == "Seller":
        print("test1")
    elif user_role == "Buyer":
        print("test2")


if __name__ == "__main__":
    main()