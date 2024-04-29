x = 0
while x < 11:
    if x < 5 and x != 0:
        print(x)
    elif x == 5:
        print("x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is:", x)
    elif x >= 5 and x <= 8:
        if x == 6:
            print(x)
        else:
            print("x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is:", x)
    if x > 8:
        print("x is bigger than 8. It is:", x)
    x = x + 1
