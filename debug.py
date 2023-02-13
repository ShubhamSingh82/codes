# decorator to log the arguments and return value of a function. 
def myfunc(func):
    def myfunc2(x,y):
        print("loading....")
        func(x,y)
        return "end of function"
    return myfunc2
@myfunc
def name(x,y):
    print(x)
    print(y)
#name = myfunc(name)
print(name(5,6))