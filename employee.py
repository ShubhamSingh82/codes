#Create an Employee class with attributes like name, age, and salary, and methods like display_employee. 
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display_employee(self):
        return f"the employee name is {self.name} and his age is {self.age} and his salary is {self.salary}"
shubham = Employee("shubham",23,28)
print(shubham.display_employee())