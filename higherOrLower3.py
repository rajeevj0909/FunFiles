#Higher Or Lower Game - CodeLab 2020
#Uses: variables, modules, input, while loop, conditionals, strings, functions
#try - catch errors
#What's New: main function, passing multiple arguements to functions (scope),
#reading and writing to text files

import random

def getGuess(low,high):
    '''Function to retrive user guess and if valid return it'''
    try:
        user_guess = int(input("Enter your guess: "))
        if validateGuess(user_guess,low,high):
            return user_guess
        else:
            return getGuess(low,high)
    except:
        print("***Invalid input***")
        return getGuess(low,high)
        

def validateGuess(user_guess,low,high):
    '''Function to valudate a guess which is passed above returns true
    or false'''
    if user_guess < low or user_guess > high:
        print("***Guess out of range***")
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
    
    data[1] = str(highScore)

    file = open("hi-scores.txt", "w")
    file.write("\n".join(data))
    file.close()
    

def main():
    #get the high score (second line in the hi-scores.txt file)
    file = open("hi-scores.txt", "r")
    data = []
    for line in file:
        data.append(line)
    file.close()
    highScore = int(data[1].strip())
    
    #enter your own limits for the game
    low = int(input("Enter Lower Bound: "))
    high = int(input("Enter Upper Bound: "))
    
    while True:
        guesses = 0
        comp_gen = random.randint(low,high)
        user_guess = getGuess(low,high)
        guesses += 1

        while user_guess != comp_gen:
            if user_guess > comp_gen:
                print("Too High! ", end = '')
                user_guess = getGuess(low,high)
            else:
                print("Too Low! ", end = '')
                user_guess = getGuess(low,high)
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
