# Write a function that takes two numbers as parameters returns a list  of n smallest odd integers
# greater than or equal to start, in ascending order.
# Example:
# Myfunc(4, 10)
#
# Output:
# [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]

def sorting_function(starting_num, number_of_elements):
    list_odd = []
    list_even = []
    for i in range(starting_num, (starting_num + 2 * number_of_elements)):
        if i % 2 != 0:
            list_odd.append(i)
        else:
            list_even.append(i)

    return list_odd, list_even


print(sorting_function(5, 11))
