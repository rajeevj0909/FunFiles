#Welcome message
print("Welcome To the Triangle Checker, please enter the 3 lengths of the triangle.")
#Makes the length of the 1st triangle a variable
triangleOne=float(input("Enter 1st side of triangle"))
#Makes the length of the 2nd triangle a variable
triangleTwo=float(input("Enter 2nd side of triangle"))
#Makes the length of the 3rd triangle a variable
triangleThree=float(input("Enter 3rd side of triangle"))
#It says when three lengths are the same it prints equilateral triangle
if triangleOne==triangleTwo and triangleTwo==triangleThree:
		print ("It’s an equilateral triangle")
#It says when two lengths are the same it prints isosceles triangle
elif triangleOne==triangleTwo or triangleTwo==triangleThree or triangleOne==triangleThree:
	print ("It’s an isosceles triangle")
#Anything else it prints scalene triangle
else:
      print("It’s an scalene triangle")
