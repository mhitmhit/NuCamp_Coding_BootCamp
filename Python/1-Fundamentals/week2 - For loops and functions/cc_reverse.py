name = input("What is your name? ")
result =""

def reverse(name):
    global result
    if len(name) == 1:
        result = result + name[0]
        return result
    result = result + name[-1]
    name = name[:-1]
    reverse(name)
    return result

print("Your name reversed is:", reverse(name))
