class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, newName):
        self.name = newName

    def change_pin(self, newPin):
        self.pin = newPin

    def change_password(self, newPassword):
        self.password = newPassword

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.balance)

    def whithdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, receiver, amount):
        print("you are transfering", amount, receiver.name )
        print("Authentication required")
        pin = int(input("Enter your pin: "))
        if (self.pin == pin):
            print("Transfer Authorized")
            self.whithdraw(amount)
            receiver.deposit(amount)
            return True
        else:
            print("Invalid Pin")
            return False

    def request_money(self, receiver, amount):
        receiverPin = int(input("Enter receiver pin: " ))
        if (receiver.pin == receiverPin):
            requestor_password = input("enter the requestion password: ")
            if (requestor_password == self.password):
                receiver.whithdraw(amount)
                self.deposit(amount)
                return True
            else:
                print("Invalid password")
                return False
        else:
            print("Invalid Pin")
            return False




# """ Driver Code for Task 1 """
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)

# """ Driver Code for Task 2 """
# user2 = User("Jim", 4567, "codename")
# print(user2.name, user2.pin, user2.password)
# user2.change_name("Jimmy")
# user2.change_pin("0000")
# user2.change_password("spider man")
# print(user2.name, user2.pin, user2.password)

# """ Driver Code for Task 3"""
# bankUser1 = BankUser("Bob", 1234, "password")
# print(bankUser1.name, bankUser1.pin, bankUser1.password, bankUser1.balance)

# """ Driver Code for Task 4"""
# bankUser1 = BankUser("Bob", 1234, "password")
# print(bankUser1.name, bankUser1.pin, bankUser1.password, bankUser1.balance)
# bankUser1.show_balance()
# bankUser1.deposit(1000)
# bankUser1.whithdraw(300)
# bankUser1.show_balance()

# """ Driver Code for Task 5"""
# requestor = BankUser("Bob", 1234, "password")
# sender = BankUser("Jim", 4567, "password")
# sender.deposit(5000)
# print("\n"+sender.name, "balance is", sender.balance)
# print(requestor.name, "balance is", requestor.balance, "\n")
# sender.transfer_money(requestor, 1000)
# print("\n" + sender.name, "account balance is", sender.balance)
# print(requestor.name, "account balance is", requestor.balance, "\n")
# requestor.request_money(sender, 1000)
# print("\n" + sender.name, "account balance is", sender.balance)
# print(requestor.name, "account balance is", requestor.balance, "\n")
