#Calculation adding for  and returns c
def addMe(a, b):
    c=a+b
    return c
#Calculation  for subtraction and returns c
def subMe(a, b):
    c=a-b
    return c
#Calculation  for multiplication and returns c
def multMe(a, b):
    c=a*b
    return c
#Calculation  for division and returns c
def divMe(a, b):
    c=a/b
    return c
#Calculation  for powering and returns c
def powMe (a, b):
    c=a**b
#  for  and prints c
def startMe():
    print ("What two numbers do you want to use?")
    num1=int(input("Enter number 1?  "))
    num2=int(input("Enter number 2?  "))

    calculation=input("What operation do you want to you, enter the symbol.  ")
    if calculation=="+":
        c=addMe(num1, num2)
    elif calculation=="-":
        c=subMe(num1, num2)
    elif calculation=="*":
        c=multMe(num1, num2)
    elif calculation=="/":
        c=divMe(num1, num2)
    elif calculation=="^":
        c=powMe(num1, num2)
    else:
        print("ERROR")
    print(c)
startMe()
again="y"
while again=="y":
    startMe()
    again=input("Go again?  y/n?    ")
