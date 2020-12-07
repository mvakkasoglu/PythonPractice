# Write a program that randomly generates an integer
# between 0 and 100, inclusive. The program should
# prompt the user to enter a number continuously until
# the number matches the randomly generated
# number. For each user input, the program tells the
# user whether the input is too low or too high, so the
# user can choose the next input efficiently.

import random

answer = int(input("Guess the number : "))

number = random.randint(0, 100)

while number != answer:
    answer = int(input("You are wrong. Try again!"))

print("You guessed the number right!")