class Cube():
   def __init__(self, length, breadth, depth):
       self.length = length
       self.breadth = breadth
       self.depth = depth
   
   def get_area_of_face(self):
       return self.length * self.breadth
   
   def get_volume(self):
       area = self.get_area_of_face()
       return area * self.depth
    
r1 = Cube(1,2,3)
r2 = Cube(30,20,10)
print("Area of Cube Face 1:", r1.get_volume())
print("Area of Cube Face 2:", r2.get_volume())
