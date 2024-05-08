states = ["Washington", "Oregon", "California"]

for x in states:
    print(x)
print("----------------\n")

for i in range(0,len(states)):
    print(states[i])
print("----------------\n")

for x in states:
    x = x.lower()
    print(x)
print("----------------\n")

print("California" in states)
print("----------------\n")

print("California" not in states)
print("----------------\n")

states2 = ["North Carolina", "Virginia"]

best_states = states + states2
print(best_states)
print("----------------\n")

print(best_states[1:2])
print(best_states[:2])
print(best_states[1:])
print(best_states[::-1])
