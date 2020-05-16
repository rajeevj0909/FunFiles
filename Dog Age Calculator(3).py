#Makes the dog age a variable and gives a welcome message.
humanAge=int(input("Welcome to The Dog Age Calculator, what is the age of your dog in human years?"))
#If user enters 1, the age prints 14.
if humanAge == 1:
    print ("Dog Age is 14")
#If user enters 2, the age prints 22.
elif humanAge==2:
             print ("Dog Age is 22")
#If user enters 3 or more, the number as humanAge does the calculation(humanAge-2)*5+22 and prints.
else:
    dogAge=(humanAge-2)*5+22
    print ("Dog Age is",dogAge)
