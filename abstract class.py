#program to demonstrate the use of abstract base class, which is a class that cannot be instantiated 
#and can only be used as a base class for other classes. 
from abc import ABC
class ClassName(ABC):

    class Car(ABC): 
        def mileage(self): 
            pass

    class Tesla(Car): 
        def mileage(self): 
            print("The mileage is 30kmph") 
    class Suzuki(Car): 
        def mileage(self): 
            print("The mileage is 25kmph ") 
    class Duster(Car): 
         def mileage(self): 
            print("The mileage is 24kmph ") 
    class Renault(Car): 
           def mileage(self): 
                print("The mileage is 27kmph ") 

    t= Tesla () 
    t.mileage() 
    r = Renault() 
    r.mileage() 
    s = Suzuki() 
    s.mileage() 
    d = Duster() 
    d.mileage()