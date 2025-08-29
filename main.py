from user_management import User_mangemente



def main():
    user_manager = User_mangemente()
    print("Wellcome to digikala")

    input_username = input("Please enter your username")
    user_manager.login_user(username=input_username)
    while not user_manager.current_user:
       input_username = input("The username does not exists, please enter another one...")
       user_manager.login_user(username=input_username)

    user_manager.current_user.get_role()





if __name__ == "__main__":
    main()