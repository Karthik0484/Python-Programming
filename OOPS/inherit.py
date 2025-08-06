# Animal and Dog Classes

# class Animal:
#     def make_sound(self):
#         print("Some Generic animal Sound.")
#
# class dog(Animal):
#     def make_sound(self):
#         print("Bark!")
#
# A = Animal()
# A.make_sound()
# D = dog()
# D.make_sound()

#Vehicle and Car Classes

# class Vehicle:
#     def __init__(self,brand,year):
#         self.brand = brand
#         self.year = year
#     def show_details(self):
#         print(f"Brand:{self.brand},Year:{self.year}")
#
# class Car(Vehicle):
#     def __init__(self,brand,year,model):
#         super().__init__(brand,year)
#         self.model = model
#     def show_details(self):
#         print(f"Brand:{self.brand},Model:{self.model},Year:{self.year}")
#
# v1 = Vehicle("Bence",2020)
# v1.show_details()
# c1 = Car("Audi",2010,"Maruti")
# c1.show_details()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def show_Details(self):
        print(f"Name: {self.name}, Age: {self.age} ")

class Student(Person):
    def __init__(self,name,age,grade):
        super(). __init__(name,age)
        self.grade = grade
    def show_Details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject
    def show_Details(self):
        print(f"Name: {self.name}, age:{self.age}, subject:{self.subject}")

s1= Student("Karthik",20,"O")
s1.show_Details()

t1 = Teacher("Ramya",30, "OOPS")
t1.show_Details()