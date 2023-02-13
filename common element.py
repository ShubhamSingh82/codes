# find the common elements in two lists. 
list1 = [1,2,3,4]
list2 = [3,4,5,6]
list3 = []
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)