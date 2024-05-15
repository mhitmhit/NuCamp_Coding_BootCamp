state_capitals ={"washington":"olympia",
                 "oregon":"salem",
                 "california":"sacramento"}

#  prints the keys
for state in state_capitals:
    print(state)

#  prints the values
for city in state_capitals.values():
    print(city)

#  using both keys and values
for state in state_capitals:
    print(state_capitals[state], "is the capital of", state)

#  using both keys and values
for state, city in state_capitals.items():
    print(city, "is the capital of", state)
