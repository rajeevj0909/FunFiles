name=str(input("What's your name?"))
from random import randint
def add():
    num1=(randint(1,50))
    num2=(randint(1,50))
    total=num1+num2
    print(num1,"+",num2,"=")
    ans_add=int(input("What's the answer?"))
    if ans_add == total:
        print("correct")
    else:
        print("You're an idiot!")

def sub():
    num1=(randint(26,50))
    num2=(randint(1,25))
    total=num1-num2
    print(num1,"-",num2,"=")
    ans_sub=int(input("What's the answer?"))
    if ans_sub == total:
        print("correct")
    else:
        print("You're an idiot!")

def mult():
    num1=(randint(1,12))
    num2=(randint(1,12))
    total=num1*num2
    print(num1,"x",num2,"=")
    ans_mult=int(input("What's the answer?"))
    if ans_mult == total:
        print("correct")
    else:
        print("You're an idiot!")
def div():
    num1=(randint(7,12))
    num2=(randint(1,6))
    total=num1/num2
    print(num1,"/",num2,"=")
    ans_div=int(input("What's the answer?"))
    if ans_div == total:
	print("correct")
    else:
        print("You're an idiot!")

add()
sub()
mult()
div()
mult()
sub()
add()
div()
div()
add()
