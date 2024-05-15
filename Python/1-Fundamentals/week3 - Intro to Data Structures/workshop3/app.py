from donations_pkg import homepage
from donations_pkg.user import login, register

database = {"admin":"password123"}
donations = []
authorized_user = ""

while(True):
    homepage.show_homepage()

    if (authorized_user == ""):
        print("You must be logged in to donate.")
    else:
        print("Logged in as: ", authorized_user)

    user_selection = int(input("Choose an option: "))

    if (user_selection == 1):
        username = input("Enter useranme: ")
        password = input("Enter password:")
        authorized_user = login(database, username, password)

    elif (user_selection == 2):
        username = input("Enter useranme: ")
        password = input("Enter password:")
        authorized_user = register(database, username)
        if (authorized_user != ""):
            database[username] = password

    elif (user_selection == 3):
        if (authorized_user == ""):
            print("\nYou are not logged in")
        else:
            donation_sting = homepage.donate(authorized_user)
            donations.append(donation_sting)

    elif (user_selection == 4):
        homepage.show_donations(donations)

    elif(user_selection == 5):
        print("Leaving DonateMe ....GoodBye !!")
        break
