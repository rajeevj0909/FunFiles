#Inputs the number
full_number = str(input("Please enter a four digit number."))
#Import library
import itertools
#Creates blank list
unique=[]
#Gets each combination in the large list
for a_pin in ((list(itertools.permutations(full_number,4)))):
        #If pin isn't in unique
        if a_pin not in unique:
                #Adds pin to unique
                unique.append(a_pin)
#Every pin in unique list
for a_pin in unique:        
        #Gets each digit from that combination
        for digit in a_pin:
                #Prints the digit and doesn't start a new line
                print(digit,end="")
        #Starts a new line
        print("")
