# program to check if a string is a palindrome using a while loop. 
n = input("enter string to check palindrome")
reverse = ""
i = len(n)
while(i>0):
    reverse = reverse + n[i- 1]
    i = i - 1
print(reverse)
if(n == reverse):
    print("the given string is palindrome")
else: 
    print("its not a palindrome")