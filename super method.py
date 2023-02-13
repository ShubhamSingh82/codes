#program to demonstrate the use of super method, which allows a derived class to call a method in the base class. 
# if we want to print more things with special 
class A :
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "i am inside class A's constructor"
        self.classvar1 = "instance variable in class A"
        self.special = "Special"
class B(A):
    classvar1 =  "i am in class B"
    def __init__(self):
        super().__init__()
        #self.var1 = "I am inside class B's constructor"
        #self.classvar1 = "instance var in class B"
a = A()
b = B()
print(b.special,b.var1,b.classvar1)