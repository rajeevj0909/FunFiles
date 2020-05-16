'''login=False
while login==False:
    user=input("User Name ?")
    password=input("Password ?")
    if user=="Bob" and password=="12345":
        break
    print ("please try again")
print ("Welcome Bob")'''

'''import math
num=int(input("Initial x :"))
rows=int(input("Number of rows:"))
spaces=float(input("Spacing   :"))
print ("       x   exp(x)")
x=num
for i in range(rows):
   print ("%8.2f %8.2f"%(x,math.exp(x)))
   x = spaces + x'''


'''num=int(input("Enter an integer :"))
total=1
for i in range(num,0,-1):
    total=total*i

print("The factorial of %d is %d."%(num,total))'''

'''sum = 0
num=1
count=0
while num>=0:
   num = int(input("Enter a number :") )
   if num<0:
       break
   sum = sum + num
   count=count+1
   mean = sum / count
if sum==0:
    print("no number has been entered")
else:
    print ("Sum is %d and Mean is %1.2f"%(sum,mean))'''

'''count = int(input())
total=0
while count>0:
    total=total+count
    print (count, total)
    count = count - 1
print ("Blast-off")'''


'''W=float(input("width ?:"))
L=float(input("length ?:"))
if W>100 or L>100:
    print("width and length must be less 100")
elif W>L:
    print("Length must be greater than Width")
elif W<0 or L<0:
    print("you should enter a positive number")
else:
    area=W*L
    print("Area is %.2f"%area)'''

'''import math
print ("       x   exp(x)")
for i in range (0,7):
    x=float(i/2)
    exp = math.exp(x)
    print ("    %3.2f    %5.2f"%(x,exp))'''

'''date=False
while date==False :
    n=int(input ("When did Columbus sail the ocean blue?"))
    if n ==1492:
        date=True
    else:
        print ("Try again ")
print ("Well done")'''

'''repeat=int(input("How many numbers ?"))
sum =0
count=0
while count<repeat:
   n=int(input("Enter a number :"))
   sum=sum+n
   count = count + 1
print ("Mean =",float(sum/repeat))'''

'''start=int(input("Please enter the starting value:"))
count = 1
while count<=start:
   print (start)
   start = start - 1
print ("Blast-off")'''


'''day=input("Day ?")
date=int(input("Date ?"))
if date==13 and day=="Friday":
    print("Be Careful")
else:
    print("Have a Nice Day")'''

'''count=0
while count<5:
    print ("hello")
    count+=1'''

'''for i in range(5,0,-1):
    print(i)
print("Blast-off")'''


