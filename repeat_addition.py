import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
# print("What is {} + {}?".format(num1, num2))
answer = int(input("What is {} + {}? ".format(num1, num2)))

# if answer == (num1 + num2):
#     print("Good job!")
# else:
#     print("Try again!")

while answer != (num1 + num2):
    answer = int(input("Try again! Enter your answer : "))

print("Good job!")