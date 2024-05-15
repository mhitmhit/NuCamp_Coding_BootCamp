import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:
    selection = input("pick a card or Q to quit: ")
    if selection == "Q" or selection == "q":
        break
    card = random.choice(diamonds)
    diamonds.remove(card)
    hand.append(card)
    print("Remaining cards:",diamonds)
    print("your hand:",hand)

    if not diamonds:
        print("\nThere are no more cards to pick")
