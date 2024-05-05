import random

print(random.randint(1,10))
random.randint(1,10)

#  returns a random value from list
pets = ["cat", "dog"]
print(random.choice(pets))

# returns same list, but shuffled
random.shuffle(pets)
print(pets)
