#program that checks the strength of a password,
#  using conditions to ensure it meets certain criteria
#  (e.g. length, special characters, etc.).
import re
s = input("enter your password")
while(True):
    if(len(s)<=8):
        print("password is week please enter password greater than 8 words")
        break
    elif not re.search("[a-z]",s):
        print("password is week please use combination of uppercase,lowercase,numeric and special case")
        break
    elif not re.search("[A-Z]",s):
        print("password is week please use combination of uppercase,lowercase,numeric and special case")
        break
    elif not re.search("[0-9]",s):
        print("password is week please use combination of uppercase,lowercase,numeric and special case")
        break
    elif not re.search("[_@$]",s):
        print("password is week please use combination of uppercase,lowercase,numeric and special case")
        break
    elif re.search("\s",s):
        print("password is week please use combination of uppercase,lowercase,numeric and special case")
        break
    else:
        print("password is strong")
        break