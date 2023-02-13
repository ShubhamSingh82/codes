#program to find all the prime numbers in a given range using a for loop. 
x = int(input("enter the first number"))
y = int(input("enter the last number"))
for i in range(x,y):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)