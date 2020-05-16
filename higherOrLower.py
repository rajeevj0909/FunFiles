#Higher Or Lower Game - CodeLab 2020
#Uses: variables, modules, input, while loop, conditionals, strings
#Development: change limits, add validation, high score

import random

guesses = 0
comp_gen = random.randint(1,100)
user_guess = int(input("Enter your guess: "))
guesses += 1

while user_guess != comp_gen:
    if user_guess > comp_gen:
        user_guess = int(input("Too High! Try again: "))
    else:
        user_guess = int(input("Too Low! Try again: "))
    guesses += 1

print("Correct! It took you: %s guess(es)" %guesses)
