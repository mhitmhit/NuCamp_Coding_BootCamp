character_list = ("wizard", "elf", "human")

wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
    print("*************************************")
    print("1) wizard")
    print("2) elf")
    print("3) human")
    character = input("choose a character: ")

    if (int(character) == 1):
        my_character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif (int(character) == 2):
        my_character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif (int(character) == 3):
        my_character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print ("Unknow character")

print("You have chosen the character: " + my_character)
print("health: " + str(my_hp))
print("damage: " + str(my_damage) +"\n")

while True:


    dragon_hp = dragon_hp - my_damage
    print("The", my_character, "damaged the Dragon!")
    print("Teh Dragon's hitpoints now are: " + str(dragon_hp) + "\n")

    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at "+my_character)
    print("The "+my_character+" hitpoints are now: " + str(my_hp) + "\n")

    if my_hp <= 0:
        print("The "+my_character+" has lost the battle")
        break
