from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("    === Automated Teller Machine ===    ")
name = input("Enter name to register: ")
pin = input("Enter pin: ")
balance = 0
print(name, "has been registered with a starting balance of", balance)

while(True):
    print("LOGIN")
    userName = input("Enter name: ")
    userPin = input("Enter PIN: ")
    if (userName == name and userPin == pin):
        print("Login successful!")
        break
    else:
        print("Invalid credentials")

while(True):
    atm_menu(name)
    option = input("Choose an option: ")
    option = int(option)
    if (option == 1):
        account.show_balance(balance)
    elif (option == 2):
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif (option == 3):
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif (option == 4):
        account.logout(name)
        break
    else:
        continue
