from file_management import Saver, Loader
class User_mangemente:
    def __init__(self):
        self.users_list = Loader.load_users()
    
    def add_user(self, user):
        self.users_list.append(user)
        Saver.save_users(self.users_list)


class User:
    def __init__(self , username , role : None) :
        self.username = username
        self.role = role

    def get_role(self) :
        return self.role
    

class Buyer(User):
    def __init__(self, username) :
        super().__init__(username, "Buyer")
        self.order_list = []


class Seller(User):
    def __init__(self, username):
        super().__init__(username, "Seller")
        self.product_list = []
