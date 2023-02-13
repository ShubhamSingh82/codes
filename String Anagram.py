#program that determines whether two strings are anagrams of each other, 
# ignoring white space and special characters. 
string1 = input("enter first string")
string2 = input("enter second string")
str1 = sorted(string1)
str2 = sorted(string2)
print(string1)
if(str1 == str2):
    print("both strings are anagram of each other")
else:
    print("these are not anagram to each other")
