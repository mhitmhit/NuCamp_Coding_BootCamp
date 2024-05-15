state_capitals ={"washington":"olympia",
                 "oregon":"salem",
                 "california":"sacramento"}
print(state_capitals)
print(len(state_capitals))

print(state_capitals["washington"])

state_capitals["washington"] = "aberdeen"
print(state_capitals)

state_capitals["texas"] = "austin"
print(state_capitals)

del state_capitals["california"]
print(state_capitals)

# pop method return a value and deletes the entry from list
removed = state_capitals.pop("texas")
print(state_capitals)
print(removed)
