#Import library
import itertools
#For every pin in a list that has had duplicates removed and every combination created from a question the user has inputted
for a_pin in list(set(((list(itertools.permutations(input("Please enter a four digit number."),4)))))):        
        #Gets each digit from that pin
        for digit in a_pin:
                #Prints the digit and doesn't start a new line
                print(digit,end="")
        #Starts a new line
        print("")
