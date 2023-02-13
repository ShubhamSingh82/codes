#program to demonstrate method overriding, where a method in the derived class has the same name as a method in the base class. 
class A :
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "i am inside class A's constructor"
        #instance varible
        self.classvar1 = "instance variable in class A"
class B(A):
    classvar1 =  "i am in class B"
    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "instance var in class B"
a = A()
b = B()
print(b.classvar1)