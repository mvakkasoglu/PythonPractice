# Write a program that reads and calculates the sum
# of an unspecified number of integers. The input 0
# signifies the end of the input.

sum = 0
num1 = int(input("enter a number: "))
sum = num1 + sum


while num1 != 0:
    num2 = int(input("enter another value: "))
    num1 = num2
    sum = num1 + sum

print(sum)
