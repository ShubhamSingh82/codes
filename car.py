#Create a Car class with attributes like model, year, and make, and methods like display_car. 
class car:
    def __init__(self,model,year,make):
        self.model = model
        self.year = year
        self.make = make
    def display_car(self):
        return f"this {self.model} is launched in {self.year} and it is made by {self.make} company"
apache = car("apache rtr 160",2022,"TVS")
print(apache.display_car())