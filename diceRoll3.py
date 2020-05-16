#Dice Roll Game - CodeLab 2020
#Uses: variables, modules, input, while loop, strings, functions
#What's New: main function, reading and writing to text files

import random

def getGuess():
    '''Function to retrive user guess and if valid return it'''
    user_guess = input("Enter your guess: ")
    if validateGuess(user_guess):
        return user_guess
    else:
        print("Invalid guess try again")
        return getGuess()

def validateGuess(user_guess):
    '''Function to valudate a guess which is passed above returns true
    or false'''
    if user_guess not in ['1','2','3','4','5','6']:
        return False
    else:
        return True

def overwrite(highScore):
    '''Function to overwrite specific score in hi-scores.txt'''
    file = open("hi-scores.txt", "r")
    data = []
    for line in file:
        data.append(line)
    file.close()
    
    data[0] = str(highScore)

    file = open("hi-scores.txt", "w")
    file.write("\n".join(data))
    file.close()
    

def main():
    #get the high score (first line of hi-scores.txt)
    file = open("hi-scores.txt", "r")
    highScore = int(file.readline())
    file.close()

    while True:
        guesses = 0
        guessed = []
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
            #overwrite the high score
            overwrite(highScore)
        print("Your hi-score is: %d"%highScore)
        
        if replay != "Y":
            break
