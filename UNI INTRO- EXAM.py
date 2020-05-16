
#print("")
#num1=int(input(""))
#for i in range():
#math.e   math.pi  math.radians()  math.sin() math.exp()/e^x
#import math

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
list1=[]
for num in range(1,num1+1):
    if num1%num==0:
        list1.append(num)
print("Factors of first number is",list1)
list2=[]
for num in range(1,num2+1):
    if num2%num==0:
        list2.append(num)
print("Factors of second number is",list2)
high=0
for num1 in list1:
    for num2 in list2:
        if num1==num2:
            high=num1
print("highest common factor is",high)



'''
shopping = [] # Start with an empty list
while True:
    s = input("Please choose from the following options:"
        +"\n'a' - add an item to the shopping list"
        +"\n'd' - delete an item"
                +"\n'q' - quit\n")
    if s=="q":
        break
   
    elif s=="a":
        i = input("Enter the name of the item to add to the shopping list"
             +"\n(or q to return to the main menu):")
        if i=="q":
            print("<--")
        elif i not in shopping:
            shopping.append(i)
            shopping.sort()
            print (shopping)
        else:
            print ("Item - " + i + " - is already in the shopping list")
            print (shopping)
    elif s=="d":
        item=str(input("Enter the name of the item to delete from the shopping list\n(or q to return to the main menu):"))
        if item=="q":
            print("<--")
        elif item in shopping:
            shopping.remove(item)
            print(item,"deleted")
            print(shopping)
        else:
            print("Item -",item,"- not found in list")
            print(shopping)
               
    else:
            print ("sorry no such option")'''


'''
max = 20
secret_number = 15
print ("Guess my number (0 -",max ,")")
attempt=3
while attempt>0 :
    guess =int(input ("Guess :"))
    if guess ==secret_number:
     print (" Spot on! Well done !")
     break
    else:
        attempt=attempt-1
        if guess>secret_number:
            if guess-secret_number<3:
                print("too close")
            print("high")
        elif guess<secret_number:
            if secret_number-guess<3:
                print("too close")
            print("low")
        if attempt!=0:       
            print(attempt," attempts left")
       
if attempt==0:
    print("sorry: play again")'''

'''
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1>num2:
    temp=num1
    num1=num2
    num2=temp
if num1%2==0:
    num1=num1+1
else:
    num1=num1+2
for i in range(num1,num2,2):
    print(i)'''




'''
title=str(input("Please enter your job title:"))
sal=int(input("Please enter your salary:"))
titleC=str(input("Please enter the job title of your colleague:"))
salC=int(input("Please enter the salary of your colleague:"))
if title==titleC:
    if sal==salC:
        print("it is fair")
    elif sal>salC:
        diff=sal-salC
        print("Your colleague is earning ",diff," pounds less than you.")
    elif salC>sal:
        diff=salC-sal
        print("Your colleague is earning ",diff," pounds more than you.")

else:
    print("not comparable")'''





'''
import math

num1=float(input("Enter the value of radius :"))
area=4*math.pi*(num1**2)
print("The area of the circle is %.5f."%area)'''



'''
names=str(input("Please enter a list of city names. Use ';' to separate the names:"))
list1=names.split(";")
list1.sort()
print(list1[0],list1[len(list1)-1])'''

'''
mark=int(input("Please enter your exam mark :"))
if mark<40:
    print("Fail, you need to work hard.")
elif mark<49:
    print("Third, you need to work harder.")
elif mark<59:
    print("2:2, you can do better than that. ")
elif mark<69:
    print("2:1, well done.")
else:
    print("First, you need to help your friends.")'''



'''
#the conversion of hours into seconds.
hours=float(input("enter time in hours :"))# value in hours
one_hour_in_minutes=60
one_minute_in_seconds=60
value_in_seconds= hours * one_hour_in_minutes * one_minute_in_seconds # conversion formula
print ("%2.2f hours is  %2d seconds"%(hours,value_in_seconds))'''



'''
print("\"Let's go to the beach this afternoon!\" suggested Kara.")
print("\"I'd rather go to the zoo.\" responded Miguel.")'''

'''
char=str(input(""))
print(char*5+"H"+char*5+"H"+char*5+"H"+char*5)
print(char*5+"H"+char*5+"H"+char*5+"H"+char*5)
print(char*5,"=Happiness=",char*5)
print(char*5,"====is=====",char*5)
print(char*5,"=Homemade==",char*5)
print(char*5+"H"+char*5+"H"+char*5+"H"+char*5)
print(char*5+"H"+char*5+"H"+char*5+"H"+char*5)'''
