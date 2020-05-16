import random
print("Welcome to The Adding Game, I will tell you if 2 numbers that are added, subtracted, divided or multiplied together equal the amount you think it is. If it is adding, type 1, if it is subtracting, type 2, if it is multiplying, type 3, if it is dividing, type 4.")
sign=int(input("Type in the number you would like to use? "))
if sign==1:
   number_1=random.randint(1,10)
   number_2=random.randint(1,10)
   number_3=number_1+number_2
   print("The first number is",number_1)
   print("The second number is",number_2)
   number_4=int(input ("What do these numbers equal when added together?"))
   if number_4==number_3:
      print("YES, CONGRATULATIONS! This is correct.")
   else:
      print("Sorry, this is incorrect.")
if sign==2:
   number_6=random.randint(1,10)
   number_7=random.randint(1,10)
   number_8=number_6-number_7
   print("The first number is",number_6)
   print("The second number is",number_7)
   number_9=int(input ("What do these numbers equal when subtracted together?"))
if number_9==number_8:
    print("YES, CONGRATULATIONS! This is correct.")
else:
    print("Sorry, this is incorrect.")
if sign==3:
   number_10=random.randint(5,10)
   number_11=random.randint(1,5)
   number_12=number_1*number_2
   print("The first number is",number_10)
   print("The second number is",number_11)
   number_12=int(input ("What do these numbers equal when multiplied together?"))
if number_12==number_11:
    print("YES, CONGRATULATIONS! This is correct.")
else:
    print("Sorry, this is incorrect.")
if sign==4:
   number_13=random.randint(1,10)
   number_14=random.randint(1,10)
   number_15=number_1/number_2
   print("The first number is",number_13)
   print("The second number is",number_14)
   number_16=int(input ("What do these numbers equal when divided together?"))
if number_16==number_15:
    print("YES, CONGRATULATIONS! This is correct.")
else:
    print("Sorry, this is incorrect.")
