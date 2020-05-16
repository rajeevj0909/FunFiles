#Menu for our games - CodeLab 2020
#Uses: variables, accessing our own modules, input, functions, conditionals,
#reading and presenting text files

import diceRoll3
import higherOrLower3
import hangman3

def menu():
    print("\n********MENU*********")
    print("1: Dice Roll")
    print("2: Higher Or Lower")
    print("3: Hang Man")
    print("4: My High Scores")
    print("5: Quit")
    choice = input("Enter your choice: ")

    #identifies the users choice then plays that game
    if choice == "1":
        print("\n***Dice Roll***\n")
        diceRoll3.main()
        menu()
    elif choice == "2":
        print("\n***Higher Or Lower***\n")
        higherOrLower3.main()
        menu()
    elif choice == "3":
        print ("==================****===============");
        print ("|__| /¯\  |\ | |¯¯   |¯\/¯| /¯\ |\ |");
        print ("|  |/¯¯¯\ | \| |__|  |    |/¯¯¯\| \|");
        print ("==================****===============");
        hangman3.main()
        menu()
    elif choice == "4":
        print("\n***My High Scores***\n")
        file = open("hi-scores.txt", "r")
        data = []
        for line in file:
            data.append(line.strip())
        file.close()
        print("Dice Roll: %s"%data[0])
        print("Higher Or Lower: %s"%data[1])
        menu()
    elif choice == "5":
        print("Thanks For Playing!!!")
        quit()
    else:
        print("***Invalid Choice Try Again***\n")
        menu()

menu()
        
    
    
