# Write a program that converts a
# Fahrenheit degree to Celsius using the
# formula:
# celsius = (5/9) * fahrenheit - 32

fahrenheit = int(input("enter fahrenheit value: "))


def temp_converter(fahrenheit):
    celcius = round((5 / 9 * (fahrenheit - 32)), 1)
    return "{} fahrenheit equals {} celcius degree".format(fahrenheit, celcius)


print(temp_converter(fahrenheit))
