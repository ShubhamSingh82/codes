# program that determines whether a given string is a palindrome 
# (i.e. reads the same forwards and backwards). 
string = input("enter any string: ")
string2 = ''
for i in string:
    string2 = i + string2
    #print(string2,end = "")
print()

if(string == string2):
    print("the given string is pallindrome")
else:
    print("it is not a pallindrome")
