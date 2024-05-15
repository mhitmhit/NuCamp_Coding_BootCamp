#  use range:
for i in range(20, -21, -5):
    print(i)

# Floor Division
    #  this is to get an integer value back, still considered a float
ZZ = _XX // Z

#  Exponentiation
X = 2 ** 2

#  Modulo
XY = Y % Z


#  accessing global scope
MYSTRING = "set in global scope"
def main():
    global MYSTRING
    MYSTRING = "Set in local scope"
main()
print(MYSTRING)

# built in functions
value = abs(-1)
value2 = float(400)
value3 = int(1.233)
value4 = max(1,2,3,4,10)
value5 = pow(2,3)
value6 = str(1223)

# function definition
def function_name():
    """prints name value """
    print("you have called function name")
def add(x,y):
    """add two values"""
    z = x + y
    print(z)

#  lambda functions
def a_function(callback):
    print(callback(3))
a_function(lambda num : num ** 2)

# importing things
    # from my_pkg import convert
    # import my_module

# Dictionary *************************************
state_capitals ={"washington":"olympia",
                 "oregon":"salem",
                 "california":"sacramento"}
    # access single element
state_capitals["washington"]
    # to add
state_capitals["new key"]="new value"
    # to delete
del state_capitals["california"]
    # pop method return a value and deletes the entry from list
removed = state_capitals.pop("texas")
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

#  Lists **************************************
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
    # looping through list
for x in states:
    print(x)
for i in range(0,len(states)):
    print(states[i])

#  sets **************************************
    #  create empty set
my_set = set()
    # create set with values
numbers_set = {1, 2, 3, 4, 4}
    #  add value to set
my_set.add(1)
    #  check if a value is in set
if (9) in numbers_set:
    print("true")

#  Strings **********************************
my_string = "alpha"
multiline_string = """bravo
charlie"""
print(my_string)
print(multiline_string)
print("pha" in my_string)
print("z" not in my_string)

#  tuples ************************************
my_tuple = (1,2,3,4,5)
    # single item tuple
my_tuple2 = (1,)
print(my_tuple[0] + my_tuple[1])
for n in my_tuple:
    print(n)
