def addMe(a, b):
    c=a+b
    return c
def subMe(a, b):
    c=a-b
    return c
def multMe(a, b):
    c=a*b
    return c
def divMe(a, b):
    c=a/b
    return c
def powMe (a, b):
    c=a**b

def startMe():
    print ("What two numbers do you want to use?")
    num1=int(input("Enter number 1?  "))
    num2=int(input("Enter number 2?  "))

    calculation=input("What operation do you want to you, enter the symbol")
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





    






































            
