# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
import math
class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass
    
class Circle(Shape):
    def __init__ (self,radius):
        self.radius=radius

    def calculate_area(self):
        return math.pi*self.radius**2
    
    def calculate_perimeter(self):
        return 2*math.pi*self.radius

class Square(Shape):
    def __init__(self,length):
        self.length=length

    def calculate_area(self):
        return self.length**2
    
    def calculate_perimeter(self):
        return 4*self.length
    
class Triangle(Shape):
    def __init__(self,base,height,side1,side2,side3):
        self.base=base
        self.height=height
        self.side1=side1
        self.side2=side2
        self.side3=side3

    def calculate_area(self):
        return 0.5*self.base*self.height
    
    def calculate_perimeter(self):
        return self.side1+self.side2+self.side3

#for circle
radius=5   
c1=Circle(radius)
print(f"\nArea of circle is {c1.calculate_area()}\n Perimeter of circle is {c1.calculate_perimeter()}\n")

#for square
length=3
s1=Square(length)
print(f"Area of square is {s1.calculate_area()}\n Perimeter of square is {s1.calculate_perimeter()}\n")

# for triangle
base=4
height=8
s1=2
s2=5
s3=4
t1=Triangle(base,height,s1,s2,s3)
print(f"Area of triangle is {t1.calculate_area()}\n Perimeter of triangle is {t1.calculate_perimeter()}\n")


