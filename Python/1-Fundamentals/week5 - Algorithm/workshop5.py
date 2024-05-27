import random

def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)
    while (tries != 0):
        print("Number of tries left:", tries)
        print("Guess a number between", start, "and", stop)
        user_guess = int(input())
        if user_guess == random_number:
            print("You guessed the correct answer")
            break
        elif user_guess < random_number:
            print("Guess Higher !")
        else:
            print("Guess Lower !")
        tries -= 1
        if tries == 0:
            print("You have failed to guess the number:", random_number)
            break

def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop)
    print("The number for the program to guess is: ", random_number)
    for x in range(1, stop+1):
        print("Number of tries left:", tries)
        print("The program is guessing...", x)
        if (x == random_number):
            print("The program has guessed the correct number!")
            break
        tries -= 1
        if tries == 0:
            print("The program failed to guess the correct number.")
            break

def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start, stop)
    print("Random number to find: ", random_number)

    lower_bound = start
    upper_bound = stop

    while (lower_bound <= upper_bound):
        pivot = (lower_bound + upper_bound) // 2
        if pivot == random_number:
            print("Found it!", pivot)
            break
        if pivot > random_number:
            upper_bound = pivot - 1
            print("Guessing lower!")
        else:
            lower_bound = pivot + 1
            print("Guessing higher!")
        tries -= 1
        if tries == 0:
            print("The program failed to find the number.")
            break

# Task 1
# guess_random_number(1, 0, 5)

# Task 2
# guess_random_num_linear(11, 0, 10)

# Task 3
guess_random_num_binary(5, 0, 100)
