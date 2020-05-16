def add(points):
    newpoints=0
    num1=(randint(1,50))
    num2=(randint(1,50))
    total=num1+num2
    print(num1,"+",num2,"=")
    ans_add=int(input("What's the answer?"))
    if ans_add == total:
        print("Correct")
        return 1
        print(newpoints)
    else:
        print("You're an idiot!")
        return 0
    return (newpoints)
    
    
def sub(points):
    newpoints=0
    num1=(randint(26,50))
    num2=(randint(1,25))
    total=num1-num2
    print(num1,"-",num2,"=")
    ans_sub=int(input("What's the answer?"))
    if ans_sub == total:
        print("Correct")
        return 1
    else:
        print("You're an idiot!")
        return 0
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
        return 1
    else:
        print("You're an idiot!")
        return 0
    print(newpoints)
        
def div(points):
    newpoints=0
    num1=(randint(50,100))
    num2=(randint(1,6))
    total=num1/num2
    print(num1,"/",num2,"=")
    ans_div=int(input("What's the answer?"))
    if ans_div == total:
        print("Correct")
        return 1
    else:
        print("You're an idiot!")
        return 0
    print(newpoints)
    
name=str(input("What's your name?"))
from random import randint
points=0
questions=10
for x in range(questions):
    choice=(randint(1,4))
    if choice==1:
        points=points+add(points)
    elif choice==2:
        points=points+sub(points)
    elif choice==3:
        points=points+mult(points)
    elif choice==4:
        points=points+div(points)
print(name,"you got ",points," / ",questions,"!")
