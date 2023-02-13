#program to demonstrate multiple inheritance, where a derived class inherits from multiple base classes. 
#here we inherit base class employee with two new classes programmer and tester and added one new property languages
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
class Tester(Employee):
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
shubham = Programmer("Shubham Singh",290,"Engineer",["python" , "java" , "sql"])
shubham.info()
manoj = Tester("Manoj Sharma",272,"Tester",["jasmine","karma","selenium"])
manoj.info()