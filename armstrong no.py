#program to check if a number is an Armstrong number using a while loop. 
x = int(input("enter number "))
sum = 0 
i = x
while(i>0):
    d = i % 10
    sum += d ** 3
    i //= 10
if x == sum:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")