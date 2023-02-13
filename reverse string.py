#program to reverse a string using a for loop.
string = input(" enter string to reverse ")
for i in range(len(string)-1,-1,-1):
    print(string[i],end ="")