class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)




class BankUser(User):
    def __init__(self, name, email, password, test):
        super().__init__(name, email, password)
        self.test = test
        self.balance = 0

    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance)

bankuser1 = BankUser("yas", "ye@gmail.com", "123pass","onetrust")
user1 = User("amy", "an32@gmail.com", "pass123")
print(bankuser1.test)
print(user1.password)
