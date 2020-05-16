#Starts function
def factorial():
    #Obtains input as integer
    number=int(input("What number would you like to enter?"))
    total=1
    #When number is zero
    if number==0:
        #This will always print 1
        print(total)
    #When number is a minus number
    elif number<0:
        #Turns number to positive so calculation can be done as though it's positive
        number=number*-1
        #Runs for loop, stops when number has decreased to 1
        for n in range(number,1,-1):
            #Total gets larger each loop
            total=total*number
            #Number decreases every loop
            number=number-1
        #Prints total as a minus
        print(total*-1)
    #When number is a positive number
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
