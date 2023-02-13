#program to generate fibonacci series using generator
n = int(input("enter number"))
def fib(x):
    a = 0
    b = 1
    for i in range(n):
        yield a 
        a,b = b, a + b
print(list(fib(n)))

