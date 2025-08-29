class User_mangemente :
    def __init__(self) :
        User = []


class User :
    def __init__(self , username , role : None) :
        self.username = username
        self.role = role

    def get_role(self) :
        return self.role
    
class Buyer(User) :
    def __init__(self, username) :
        super().__init__(username, "Buyer")
        self.order_list = []

class Seller(User) :
    def __init__(self, username):
        super().__init__(username, "Seller")
        self.product_list = []