#Higher Or Lower Game - CodeLab 2020
#Uses: variables, modules, input, while loop, conditionals, strings, functions
#try - catch errors
#What's New: function, try - except, chanigng limits, hi-score

import random

#variable for hi-score set high at first (hopefully beatable)
highScore = 100
#enter your own limits for the game
low = int(input("Enter Lower Bound: "))
high = int(input("Enter Upper Bound: "))

def getGuess():
    '''Function to retrive user guess and if valid return it'''
    try:
        user_guess = int(input("Enter your guess: "))
        if validateGuess(user_guess):
            return user_guess
        else:
            return getGuess()
    except:
        print("***Invalid input***")
        return getGuess()
        

def validateGuess(user_guess):
    '''Function to valudate a guess which is passed above returns true
    or false'''
    if user_guess < low or user_guess > high:
        print("***Guess out of range***")
        return False
    else:
        return True

while True:
    guesses = 0
    comp_gen = random.randint(low,high)
    user_guess = getGuess()
    guesses += 1

    while user_guess != comp_gen:
        if user_guess > comp_gen:
            print("Too High! ", end = '')
            user_guess = getGuess()
        else:
            print("Too Low! ", end = '')
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
