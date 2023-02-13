#program to find the sum of values in a dictionary. 
dict1 = {"a":1,"b":2,"c":3,"d":4}
sum = 0
for i in dict1.values():
    sum = sum + i 
print(sum)