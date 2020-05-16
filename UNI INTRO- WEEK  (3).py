'''import math
# this program code accepts float numbers
num=float(input("radius ?:"))
if num<0:
    print("radius is not a positive number")
else:
    c=2*math.pi*num
    if c<100:
        print("it is too small")
    else:
        print("Circumference :%4.2f"%(c))
'''
'''import math
num=int(input())
num=(num/3)*2
rad=math.radians(num)
sin=math.sin(rad)
print("sin(%d)=%.1f"%(num,sin))
'''
'''import math
a=float(input("please enter a number:"))
b=float(input("please enter a number:"))
c=float(input("please enter a number:"))
d=float(input("please enter a number:"))
print("     X |   e*X")
print("---------------")
list1=[a,b,c,d]
for letter in list1:
    print("  %6.2f |  %2.2f"%(letter,math.e*letter))
'''
'''
# program only accepts interger numbers
l=int(input("Enter length:"))
w=int(input("Enter width:"))
area=w*l #formula for the area calculation of rectangle
if l<0 or w<0:
    print("Error: Both the length and width must be positive numbers")
else:
    print("Area of the rectangle is ", area)
'''
'''
age=int(input("enter the age:"))

if age<5:
    print ("free")
elif age<18:
    print ("half-price")
elif age>65:
    print ("half-price")
else:
    print ("full price")

'''
'''
a=float(input("enter number a:"))

b=float(input("enter number b:"))

c=float(input("enter number c:"))

if (b*b==4.0*a*c):
    x1=(-b+((b*b)-4.0*a*c)**0.5)/(2.0*a)
    print("only one root. X:",x1)

elif (b*b>=4.0*a*c):

    x1=(-b+((b*b)-4.0*a*c)**0.5)/(2.0*a)
    x2=(-b-((b*b)-4.0*a*c)**0.5)/(2.0*a)
    print ("root 1:",x1,"root 2:",x2)

else:
    print ("no roots")
'''



'''x=[0.5,1.0,1.5,2.0,2.5,3.0]
print("     X |   e*X")
print("---------------")
calc=2.718*0
print("     0 |  %1.2f"%(calc))
for value in x:
    calc=2.718*value
    print("  %1.2f |  %1.2f"%(value,calc))'''


'''import math
a=int(input("enter number a:"))
b=int(input("enter number b:"))
c=int(input("enter number c:"))
left=b*b
right=4*a*c
if left<right:
    print("no roots")
else:
    quadratic1=((-1*b)+(math.sqrt((b*b)-(4*a*c))))/(2*a)
    quadratic2=((-1*b)-(math.sqrt((b*b)-(4*a*c))))/(2*a)
    print("root 1:%.3f root 2:%.3f"%(quadratic1,quadratic2) )
'''
'''
import math
angle=int(input("please enter an angle in degrees:"))
radian=math.cos(math.radians(angle))
print("cos(%1.1f)=%1.1f" %(angle,radian))'''


