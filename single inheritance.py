#program to demonstrate single inheritance, where a derived class inherits from a base class. 
class Employee:
    def __init__(self,name,salary,role):
        self.name = name 
        self.salary = salary
        self.role = role
class Programmer(Employee):
    def __init__(self,name,salary,role,languages):
        self.name = name 
        self.salary = salary
        self.role = role
        self.languages = languages
    def prog(self):
        print("details of programmer")
    def info(self):
        self.prog()
        print(f"i am {self.name} and my salary is {self.salary} and i am {self.role} and i know {self.languages}")
shubham = Programmer("shubham",29,"enginner","python")
shubham.info()