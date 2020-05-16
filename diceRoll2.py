#Dice Roll Game - CodeLab 2020
#Uses: variables, modules, input, while loop, strings, functions
#What's New: functions, hi-score

import random

def getGuess():
    '''Function to retrieve user guess and if valid return it'''
    user_guess = input("Enter your guess: ")
    if validateGuess(user_guess):
        return user_guess
    else:
        print("Invalid guess try again")
        return getGuess()

def validateGuess(user_guess):
    '''Function to validate a guess which is passed above returns true
    or false'''
    if user_guess not in ['1','2','3','4','5','6']:
        return False
    else:
        return True

#variable for hi-score cannot be more than 6
highScore = 6

while True:
    guesses = 0
    rolled_num = random.randint(1,6)
    user_guess = getGuess()
    guesses += 1

    while int(user_guess) != rolled_num:
        print("Unlucky! Try again, ", end = '')
        user_guess = getGuess()
        guesses += 1

    print("\nCorrect! It took you: %s guess(es)\n" %guesses)
    
    print("Press Y to play again or ENTER key to quit")
    replay = input("Enter choice: ").upper()

    #check to see if you beat your hi-score
    if guesses < highScore:
        highScore = guesses
    print("Your hi-score is: %d"%highScore)
    
    if replay != "Y":
        break
            

