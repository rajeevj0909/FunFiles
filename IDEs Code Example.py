#This sets the input_valid to false so that the iteration can begin
input_valid = False
#Position is set to 1, in the list this is the second value, this value and every two onward must be doubled
position = 1
#Total must be initially defined
total = 0

#This ensures that the system keeps asking for an input until this is valid
while input_valid == False:
    #Take the card number input
    cardNumber = input("Enter Card Number: ")
    #This checks that the length is 16 and this is an integer, the qualities of a valid inputs
    if len(cardNumber) == 16 and isinstance(int(cardNumber), int):
        #The input must be valid if this point is reached
        input_valid = True
        #Cast the card number as an integer for the next action to work
        cardNumber = int(cardNumber)
        #This splits the card number down into a list where every digit has its own position, this makes manipulation easier
        dig = [int(x) for x in str(cardNumber)]
    #Anything other than a true input is invalid, so reject this.
    else:
        #Give an error message to ensure the user understands is happening
        print("Please enter a valid card number! (Valid card numbers are integers of 16 digits length.")

#This reverses the list which has been formed
dig = dig[::-1]
#This allows the program to cycle through this list.
while position < len(dig):
    #Multiplies every other digit by 2 (initially set at the 2nd entry, position is incremented by 2 each time to skip one)
    digitcheck = dig[position]*2
    #If the length of this new doubles number is more than 1 then it needs to be split as DIGITS are added, not numbers
    if len(str(digitcheck)) > 1:
        #Use the same procedure to break this down into small sections
        dig[position] = [int(x) for x in str(digitcheck)]
        #This adds these two to the total, (16 would add 1 and 6 thanks to the above procedure)
        digitcheck = dig[position][0]+ dig[position][1]
    #Add this to the total, as well as the previous number, this therefore adds a total as the program cycles through the list.
    total = total + digitcheck + dig[position-1]
    #Increment the position by two to ensure that every other is doubled, then the one missed is added at the end
    position = position+2

#This checks that the total is a MODULUS of 10, therefore ensures that this is a multiple of 10, if it is then this is a valid card number
if total % 10 == 0:
    print("Valid card number")

#If the total is not a MODULUS of 10 then this is an invalid card number
else:
    print("This is not a real card number")
