# program to sort a tuple of numbers. 
tup = (21,38,46,24,26,91,75)
list1 = list(tup)
for i in range(0,len(list1)-1,1):
    min = i
    for j in range(i+1,len(list1),1):
        if list1[j]<list1[min]:
            min = j
    list1[i],list1[min] = list1[min],list1[i]
print(list1)
