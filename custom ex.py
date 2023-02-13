#program to create and raise custom exceptions
class MyError(Exception):
    pass
x = 10 
try:
    if x < 5:
        print(x)
    else:
        raise MyError
except MyError:
    print("entered value  is  greater than 5")
