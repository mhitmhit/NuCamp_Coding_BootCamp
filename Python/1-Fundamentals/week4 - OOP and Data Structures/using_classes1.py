class Player:
    #  class attributes
    max_hp = 4000


#  can change class attribute
Player.max_hp = 5000

#  create instances of objects
player1 = Player()
player1.max_hp
player2 = Player()

print(player1.max_hp)
print(player2.max_hp)
