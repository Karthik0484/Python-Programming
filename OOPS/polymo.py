# 🔴 Q5. Create a polymorphic employee payment system 💳
# Write a class Employee with subclasses Intern, Developer, Manager.
# Each should have a method calculate_salary() returning different salaries.
# Then create a payroll function that takes a list of employee objects and prints their salary

from abc import ABC,abstractmethod

class Employee(ABC):

    def __init__(self,salary):
        self.salary = salary

    @abstractmethod
    def calculate_salary(self,salary):
        print("Hello")
        pass

class Intern(Employee):
    def calculate_salary(self,salary):
        print(f"Salary of Intern is {self.salary}")

class Developer(Employee):
    def calculate_salary(self,salary):
        print("Salary of Developer is 20,000")

class Manager(Employee):
    def calculate_salary(self,salary):
        print("Salary of Manager is 50,000")

i1 = Intern(10000)
i1.calculate_salary(10000)




