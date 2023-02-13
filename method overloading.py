#program to demonstrate method overloading
def multiplication(x,y):
    l = x * y
    print(l)
def multiplication(x,y,z=1):
    m = x*y*z
    print(m)
multiplication(2,3)