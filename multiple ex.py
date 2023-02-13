#program to handle multiple exceptions in a single try-except block. 

'''try:
    list = [1,2,3,4,5]
    print(list[5])
except NameError:
    print("Name error")
except IndexError:
    print("index out of list range")'''

try:
    list = [1,2,3,4,5]
    print(list[5])
except (NameError,IndexError) as error:
    print(error)
