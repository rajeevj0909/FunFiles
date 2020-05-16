#Hangman Game - CodeLab 2020
#Uses: variables, input, while loop, conditionals, strings, for loop, lists
#What's New: including it all in main function

import random

def main():
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
        guess = input("Guess a letter: ").lower()

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

    #checks to see if they want to play again
    print("Press Y to play again or ENTER key to quit")
    replay = input("Enter choice: ").upper()
    if replay == "Y":
            main()
            

