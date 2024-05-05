def show_balance(balance):
    print("Account balance is:", balance)

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return float(amount) + balance

def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    return balance - float(amount)

def logout(name):
    print("Goodbye",name)
