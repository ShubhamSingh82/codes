#program to reverse a tuple. 
tup = (21,38,46,24,26,91,75)
list1 = list(tup)
list2 = []
for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
print(tuple(list2))
