#program to sort a dictionary by key or by value. 
dict1 = {"a": 4, "b": 2, "c": 3, "d": 11, "e": 7}
sorted_dict1 = sorted(dict1.items(), key=lambda x:x[1])

converted_dict = dict(sorted_dict1)

print(converted_dict)