#Starts function
def factorial():
    #Obtains input as integer
    number=int(input("What number would you like to enter?"))
    print(number)
    #Gives a value to total to get code ready.
    total=1
    #When number is zero
    if number==0:
        #This will always print 1
        print("1")
    #When number is any other number
    else:
        #Runs for loop, stops when number has decreased to 1
        for n in range(number,1,-1):
             #Total gets larger each loop
            total=total*number
            #Number decreases every loop
            number=number-1
        #Prints total
        print(total)

#Runs function
factorial()
