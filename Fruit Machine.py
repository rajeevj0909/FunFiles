#The random library needs to be imported in order to randomise what symbols come up.
import random
#Credit starts at £1
credit = 1.00
#Welcome message
print("Welcome to Fruit Machine!\nYou have entered £1. We take 20p for each go.\n\nWarning:Gambling excessivly is not very responsible, please know when to stop!")
#Function to go again after the first turn
def go_again(credit):
    #This list are the possible symbols that can be used by the program
    symbols = ["Cherry","Bell", "Lemon", "Orange", "Star", "Skull"]
    #Takes 20p after each go.
    credit=credit-0.20
    #Creates 3 random numbers each corresponding to a symbol from the list
    random1=random.randint(0,5)
    random2=random.randint(0,5)
    random3=random.randint(0,5)
    print(random1)
    print(random2)
    print(random3)
    #If all results are the same symbol
    if symbols[random1]==symbols[random2]==symbols[random3]:
        #If they are all skulls
        if symbols[random1]=="Skull":
            #Outputs the result
            print("YOU GOT 3 SKULLS! \nWe have taken all your money!!!\n")
            #Takes all money
            credit=credit-credit
            #Runs the menu function
            start_again(credit)
        #If all symbols are bells
        elif symbols[random1]=="Bell":
            #Outputs the result
            print("YOU GOT 3 Bells! \nWe have given you £5!!!\n")
            #Gives £5 to credit
            credit=credit+5
            #Runs the menu function
            start_again(credit)
        #If symbols are the same
        else:
            #Outputs the result
            print("You have got 3"+symbols[random1]+"s\nWe added £1!\n" )
            #Adds £1 to credit
            credit=credit+1.00
            #Runs the menu function
            start_again(credit)
    #If 2 of the symbols are the same
    elif symbols[random1]==symbols[random2] or symbols[random2]==symbols[random3]or symbols[random1]==symbols[random3]:
        #If the 2 symbols are skulls
        if (symbols[random1]=="Skull" and symbols[random2]=="Skull")or(symbols[random2]=="Skull" and symbols[random3]=="Skull")or(symbols[random1]=="Skull" and symbols[random3]=="Skull"):
            #Outputs the result
            print("You have 2 SKULLS!\nWe took £1!\n")
            #Takes £1 from credit
            credit=credit-1.00
            #Runs the menu function
            start_again(credit)
        #If 2 symbols are the same
        else:
            #Outputs the result
            print("You got 2 of the same symbols!\n We added 50p!\n")
            #Adds 50p to the credit
            credit=credit+0.50
            #Runs the menu function
            start_again(credit)
    #If all 3 symbols are different
    else:
        #Outputs the result
        print("You got 3 different symbols:\n"+symbols[random1]+"+"+symbols[random2]+"+"+symbols[random3]+"\n")
        #Runs the menu function
        start_again(credit)
        
#This function acts like a menu for the game 
def start_again(credit):
    #Checks if the credit is less than zero
    if credit<0:
        #Credit becomes zero
        credit==0
        #Ends the game
        print("You have nothing left!\n\nBYE LOSER!")
    #Checks if there is enough credit for another go    
    elif credit>0.19:
        #Outputs current credit
        print("You have £"+str(credit)+"0 left!" )
        #Checks if they want to go again
        again=str(input("Would you like to go again?\n"))
        #Validation for the input
        again.lower()
        #If answer was yes
        if again=="yes":
            #The game is run again
            go_again(credit)
        #If answer was no
        elif again=="no":
            #Ends the game
            print("Thanks for playing,you have left with £"+str(credit)+"0.\n\nADIOS!!!")
        #If the input isn't recognised
        else:
            #Outputs an error message
            print("Dunno what you mean, say a simple yes or no for god's sake!")
            #Starts the menu again
            start_again(credit)
    #If there is not enough money to play again
    else:
        #Ends the game
        print("Thanks for playing,you have left with £"+str(credit)+"0.\n\nADIOS!!!")

#Runs the first game
go_again(credit)
