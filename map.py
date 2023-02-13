#program to demonstrate the use of the map and filter functions. 
def cube(a):
    return a*a*a
def greater_20(a):
    if a >= 20:
        return a
a = [1,2,3,4,5]
result = list(map(cube,a))
result1 = list(filter(greater_20,result))
print(result)
print(result1)