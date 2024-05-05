import random

high_score = 0

def dice_game():
    while(True):
        print("current high score: ", high_score)
        print("1) roll dice ")
        print("2) leave game\n")
        choice = input("enter your choice: \n")
        choice = int(choice)
        if (choice ==2):
            print("\nGoodbye")
            break
        elif (choice == 1):
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            latestScore = dice1 + dice2
            print("you roll a...", dice1)
            print("you roll a...", dice2)
            print("\nyou have rolled a total of:", latestScore)
            if (latestScore > high_score):
                print("\nNew high score !")

dice_game()
