# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.from datetime import date
from datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob

    def calculate_age(self):
        current_year=date.today().year
        age=current_year-self.dob
        return age
    
name=input("Enter your name: ")
country=input("Enter your and country: ")
dob=int(input("Enter your date of birth: "))
age=Person(name,country,dob)
print(f"{age.name} is {age.calculate_age()} years old")