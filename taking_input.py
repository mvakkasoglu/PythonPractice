def method_input():
    print("Enter a value:")
    my_value = input()
    print("You entered {}".format(my_value))


def method_input_with_message():
    my_value = input("Enter a value: ")
    print("You entered ", my_value)


def input_casing():
    my_value = input("input a number: ")  # let’s input a number
    print(type(my_value))  # prints <class 'str'>
    my_value = int(input("input a number: "))  # using int() function
    print(type(my_value))  # prints <class 'int'>
    my_value = eval(input("input a number: "))  # using eval() function
    print(type(my_value))  # prints <class 'int'>


method_input()
method_input_with_message()
input_casing()
