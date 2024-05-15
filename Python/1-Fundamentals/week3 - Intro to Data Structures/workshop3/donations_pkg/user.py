def login(database, username, password):
    if (username in database):
        if (database[username] == password):
            print("\nWelcome back", username)
            return username
        else:
            print("\nincorrect password ...!!")
            return ""
    else:
        print("\nusername not found ... !!\n")
        return ""

def register(database, username):
    if (username in database):
        print("\nUsername already registered")
        return ""
    else:
        print("\nuseranme successfully registerd")
        return username
