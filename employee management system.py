#Employee Management system
class Employee:

    def get_employee(self):
        self.id = input("id: ")
        self.name = input("name: ")
        self.salary = input("salary: ")
        self.department = input("department: ")
        self.phone = input("phone: ")
        self.email = input("email: ")
    def insert_data(self):
        print(self.id, self.name, self.salary)
    def Search_data(self, id):
        if id == self.id:
            return True
        else:
            return False
    def get_data(self):
        print(f"employee name is {self.name} he gets salary {self.salary} and department is {self.department}")
    def get_contact(self):
        print(f"{self.name} has phone number {self.phone} and email {self.email}")
    def get_department(self):
        print(f"{self.name} works in the {self.department} department")
n = int(input("Enter Total No. of Employees?"))
L = list()
for i in range(n):
    E = Employee()
    E.get_employee()
    L.append(E)
id = input("Enter Id U Want to Search?")
for x in L:
    found_data = x.Search_data(id)

    if (found_data):
        z = input("what information you want for full info enter a , c for only contact and d for department")
        if z == "a":
            x.get_data()
            break
        elif z == "c":
            x.get_contact()
            break
        elif z == "d":
            x.get_department()
            break
        else:
            print("enter a for full info or enter e for contact only")
            break
if (not found_data):
    print("Employee Not Exist")