#find the unique elements in a list. 
list =[1,2,3,4,4,6,3,5,6,7,8,7]
list1 = []
for i in list:
    if(list.count(i)<=1):
        list1.append(i)
print(list1)
        