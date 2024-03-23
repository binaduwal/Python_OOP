# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def add(self,x,y):
        return x+y
    
    def subtract(self,x,y):
        return x-y
    
    def multiply(self,x,y):
        return x*y

    def divide(self,x,y):
        if y!=0:
            return x/y
        else:
            return("Cannot divide by Zero.")


num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
o1=Calculator(num1,num2)
print(f"Add: {o1.add(num1,num2)}")
print(f"Subtract: {o1.subtract(num1,num2)}")
print(f"Multiply: {o1.multiply(num1,num2)}")
print(f"Division: {o1.divide(num1,num2)}")

