# program to print a pyramid using nested loops. 
x = 30
y = x - 1
for i in range(0,x):
    for j in range(0,y):
        print(" ",end ="")
    y = y - 1
    for j in range(0,i+1):
        print("*",end =" ")
    print("")
