print('Welcome! This is logic gates')
def funcOR():
    A=int(input('What is the first input'))
    B=int(input('What is the second input'))
    if A==1 or B==1:
        print('1, is the output')
    elif A==0 and B==0:
        print('0, is the output')
    else:
        ('Incorrect input')
def funcAND():
    A=int(input('What is the first input'))
    B=int(input('What is the second input'))
    if A==0 and B==0:
        print('0, is the output')
    elif A==0 and B==1:
        print('0, is the output')
    elif A==1 and B==0:
        print('0, is the output')
    elif A==1 and B==1:
        print('1, is the output')
    else:
        ('Incorrect input')
def funcNOT():
    A=int(input('What is the first input'))
    B=int(input('What is the second input'))
    if A==0:
        print('1, is the output')
    elif A==1:
        print('0, is the output')
    else:
        ('Incorrect input')
logicL=input('Enter logic gate')
logic=logic.upper()
if logic == "OR":
    funcOR()
if logic == "AND":
    funcAND()
if logic == "NOT":
    funcNOT()
