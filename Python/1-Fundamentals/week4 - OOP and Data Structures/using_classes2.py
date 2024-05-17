class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0

player1 = Player("aaron", 10000)
player2 = Player("amy", 15000)

print(player1.hp)
