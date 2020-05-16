#Hangman Game - CodeLab 2020
#Uses: variables, input, while loop, conditionals, strings, for loop, lists

#Fancy title screen
print ("==================****===============")
print ("|__| /¯\  |\ | |¯¯   |¯\/¯| /¯\ |\ |")
print ("|  |/¯¯¯\ | \| |__|  |    |/¯¯¯\| \|")
print ("==================****===============")

import random

def getGuess():
    '''Function to retrieve user guess and if valid return it'''
    user_guess = input("Enter your guess: ")
    if validateGuess(user_guess):
        return user_guess.lower()
    else:
        print("Invalid guess try again must be a single letter of the alphabet")
        return getGuess()

def validateGuess(user_guess):
    '''Function to validate a guess which is passed above returns true
    or false'''
    if user_guess.isalpha() and len(user_guess) == 1:
        return True
    else:
        return False


#get a random words from a list of words
words = ["Jazz", "Apple", "Character", "Rhythm", "CodeLab", "Piano"]
word = random.choice(words)

guessed = []
GuessedWord = list(len(word)*"_")
wordAsList = list(word.lower())
lives = 8

while True:
    print("\n \n")

    #check if player is out of lives
    if lives == 0:
        print("Game over")
        break

    #check if player has guessed all the letters
    if GuessedWord == wordAsList:
        print(" ".join(GuessedWord))
        print("You Win!!!")
        break

    print(" ".join(GuessedWord))
    print("Lives Remaining: %d"%(lives))
    print(" ".join(guessed))
    guess = getGuess()

    #check that the letter has not already been guessed
    if guess not in guessed:
        guessed.append(guess)
        #check if guessed letter is incorrect
        if guess not in wordAsList:
            lives = lives - 1
        #if it is correct fill in the relevant spaces with it
        else:
            for i in range(0,len(wordAsList)):
                if guess == wordAsList[i]:
                    GuessedWord[i] = guess
    else:
        print("You have already guessed that")

