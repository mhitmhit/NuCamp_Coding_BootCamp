def linear_search_dictionary(dictionary, target):
    for x,y in dictionary.items():
        if (y == target):
            print("Found item at ", x)
            return None
    else:
        print("Target not in dictionary")

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
