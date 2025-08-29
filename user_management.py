from file_management import Saver, Loader

class User_management:
    def __init__(self):
        self.users_list = Loader.load_users()
        self.current_user = None
    
    def add_user(self, user):
        self.users_list.append(user)
        Saver.save_users(self.users_list)

    def login_user(self , username) :
        for user in self.users_list :
            if user.get_username() == username:
                self.current_user = user
                return user
        return None

    def sing_up_user(self, username, role) :
        new_user = User(username, role)
        self.add_user(new_user)

class User:
    def __init__(self , username , role : None) :
        self.username = username
        self.role = role

    def get_role(self) :
        return self.role
    
    def get_username(self) :
        return self.username
    

class Buyer(User):
    def __init__(self, username) :
        super().__init__(username, "Buyer")
        self.order_list = []


class Seller(User):
    def __init__(self, username):
        super().__init__(username, "Seller")
        self.product_list = []
