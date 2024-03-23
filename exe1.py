#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return math.pi*self.radius**2
    
    def perimeter(self):
        return (self.radius*2*math.pi)

c1=Circle(4)
print(f"Area of circle is {c1.area()} and perimeter of circle is {c1.perimeter()}")
    
    
