def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x] == target:
            print("item found in ", x)
            return x
    print("target not in the list")
    return -1

my_list = [6, 3, 4, 2, 5, 7]
linear_search(my_list, 5)
linear_search(my_list, 3)
linear_search(my_list, 8)

print(my_list.index(11))
