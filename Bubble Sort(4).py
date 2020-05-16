print('welcome to the bubble sort')
numberList=[1, 3, 2, 4,8,5,11, -7,-1, 234, -3]


#Rajeev&Kishan//Bubble sort
def bubblesort(numberList):
#Creates a function called 'bubblesort' this will sort the list in a specific way.
    for element in range (len(numberList)-1, 0, -1):
    #For how many numbers there are in the list...
        print (numberList)
        for i in range(element):
        #For each number in the list...
            if int(numberList[i])>int(numberList[i+1]):
            #If the current number is bigger than the number ahead...
                temp = numberList[i]
                #Create the variable 'temp' and store the number ahead's value.
                numberList[i] = numberList[i+1]
                #Change the current number to the one ahead.
                numberList[i+1] = temp
                #Change the number ahead to the current number.
                
#Creates the list.
bubblesort(numberList)
#Runs the function
print(numberList)
#Outputs the list.
