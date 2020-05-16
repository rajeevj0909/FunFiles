#User's input
number=str(input("Whats your numbers"))
#Creates empty list for sequence of digits
number1=[]
#For every digit in the number
for digit in number:
    #Turns it into an interger
    digit = int(digit)
    #Adds it to the list
    number1.append(digit)
#Creates a counter
count=0
#Creates a running total
total=0
#Creates a number of the length of the array
length=len(number1)
#Runs only for the length of the list
while count<length-1:
    #If 2 consecutive digits are equal
    if number1[count]==number1[count+1]:
        #Adds the total and the equal number
        total=total+number1[count]
    #Moves onto next number
    count=count+1
#If last number and the first number are the same
if number1[length-1] == number1[0]:
    #Adds that number to the total
    total = total + int(number1[0])
#Prints the total
print(total)
