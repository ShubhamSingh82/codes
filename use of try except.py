#program to demonstrate the use of try and except blocks
#to handle exceptions. 

try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
except:
    print("Error:please check your values")