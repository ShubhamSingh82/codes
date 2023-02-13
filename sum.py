#program to find the sum of N numbers using a for loop. 
n = int(input("enter the number"))
sum = 0
for i in range(n+1):
    sum = sum + i
print(sum)