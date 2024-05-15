def show_homepage():
    print("\n === DonateMe Homepage === ")
    print("------------------------------------------")
    print("| 1. Login | 2. Register |")
    print("------------------------------------------")
    print("| 3. Donate | 4. Show Donations |")
    print("------------------------------------------")
    print("| 5. Exit |")
    print("------------------------------------------")

def donate(username):
    donation_amt = input("\nEnter amount to donate: ")
    dontation_string = username + " donated "+ donation_amt
    print("Thank you for your donation !")
    return dontation_string

def show_donations(donations):
    print("\n-----All Donations-----")
    if (len(donations) == 0):
        print("Currently, there are no donations")
    else:
        for gift in donations:
            print(gift)
