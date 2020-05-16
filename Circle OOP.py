class Circle:
    def __init__(Circle,r):
        Circle.radius=r
        
    def getDiameter(Circle,r):
        diam=r*2
        return ("Diameter: ",diam)
    def circum(Circle,r):
        circum=2*r*3.14159265359
        return("Circumference: ",circum)
    def area (Circle,r):
        area=r*r*3.14159265359
        return("Area: ",area)

r=float(input("What's the radius?"))
c = Circle(r)
print(c.getDiameter(r))
print(c.circum(r))
print(c.area(r))
        
