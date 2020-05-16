#Dice Roll Game - CodeLab 2020
#Uses: variables, modules, input, while loop, strings
#Development: validation

import random

guesses = 0
rolled_num = random.randint(1,6)
user_guess = int(input("Enter your guess: "))
guesses += 1

while user_guess != rolled_num:
    user_guess = int(input("Incorrect, try again: "))
    guesses += 1

print("Correct it took you: %s guess(es)" %guesses)

