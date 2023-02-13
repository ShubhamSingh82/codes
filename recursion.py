#program to calculate the factorial of a number using recursion. 
def fact(n):
    if(n==1):
        return n
    else:
        return n * fact(n-1)
print(fact(10))