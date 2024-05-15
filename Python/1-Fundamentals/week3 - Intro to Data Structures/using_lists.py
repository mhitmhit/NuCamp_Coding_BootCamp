states = ["Washington", "Oregon", "California"]

print(states[-1])

print(len(states))

states.append("new york")
print(states)

# removes last item, and returns it
states.pop()
print(states)

# add item to end of list
states.append("new york")
print(states)

states.pop(0)
print(states)

# insert item at a specific index
states.insert(0, "north carolina")
