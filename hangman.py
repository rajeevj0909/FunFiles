#Hangman Game - CodeLab 2020
#Uses: variables, input, while loop, conditionals, strings, for loop, lists
#Development: draw hangman character, display guessed letters, more words
#randomly generated, make it a 2-player game

#Fancy title screen
print ("==================****===============");
print ("|__| /¯\  |\ | |¯¯   |¯\/¯| /¯\ |\ |");
print ("|  |/¯¯¯\ | \| |__|  |    |/¯¯¯\| \|");
print ("==================****===============");


word = "Jazz"
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
        print("You Win!!!")
        break

    print(" ".join(GuessedWord))
    print("Lives Remaining: %d"%(lives))
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
