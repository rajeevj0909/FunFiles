def add(points):
    newpoints=0
    num1=(randint(1,50))
    num2=(randint(1,50))
    total=num1+num2
    print(num1,"+",num2,"=")
    ans_add=int(input("What's the answer?"))
    if ans_add == total:
        print("Correct")
        newpoints=points+1
    else:
        print("You're an idiot!")
    return (newpoints)
    print(newpoints)
    
def sub(points):
    newpoints=0
    num1=(randint(26,50))
    num2=(randint(1,25))
    total=num1-num2
    print(num1,"-",num2,"=")
    ans_sub=int(input("What's the answer?"))
    if ans_sub == total:
        print("Correct")
        newpoints=points+1
    else:
        print("You're an idiot!")
    return (newpoints)
    print(newpoints)

def mult(points):
    newpoints=0
    num1=(randint(1,12))
    num2=(randint(1,12))
    total=num1*num2
    print(num1,"x",num2,"=")
    ans_mult=int(input("What's the answer?"))
    if ans_mult == total:
        print("correct")
        newpoints=points+1
    else:
        print("You're an idiot!")
    return (newpoints)
    print(newpoints)
        
def div(points):
    newpoints=0
    num1=(randint(7,12))
    num2=(randint(1,6))
    total=num1/num2
    print(num1,"/",num2,"=")
    ans_div=int(input("What's the answer?"))
    if ans_div == total:
        print("Correct")
        newpoints=points+1
    else:
        print("You're an idiot!")
    return (newpoints)
    print(newpoints)

name=str(input("What's your name?"))
from random import randint
points=0
for x in range(10):
    choice=(randint(1,4))
    if choice==1:
        newpoints=add(points)
    elif choice==2:
        newpoints=sub(points)
    elif choice==3:
        newpoints=mult(points)
    elif choice==4:
        newpoints=div(points)
print(name,"you got ",newpoints,"!")
