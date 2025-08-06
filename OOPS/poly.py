
#  Method Overriding (Inheritance-based)

# class Employee:
#     def show_role(self):
#         print("General Employee.")

# class Manager(Employee):
#     def show_role(self):
#         print("Manager of the team.")

# E1 = Employee()
# E1.show_role()

# M1 = Manager()
# M1.show_role()

#Method Overloading (Using Default Arguments)

class MathOperation1:
    def add(self,*args):
        total = 0
        for num in args:
            total += num

        print("Sum: ", total)

mat = MathOperation1()
mat.add(1,2)


