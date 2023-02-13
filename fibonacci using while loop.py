# program to find fibonacci series from while loop (0,1,1,2,3,5)
x = 0
y = 1
n = 5
i = 0
print(x,y,end = " ")
while(i<=n):
    z = x + y
    x = y
    y = z
    i = i + 1
    print(z,end = " ")