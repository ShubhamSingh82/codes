#program to find the maximum and minimum element in a tuple. 
tup = (21,38,46,24,26,91,75)
max = tup[0]
min = tup[0]
for i in tup:
    if i > max:
        max = i
    if i < min:
        min = i
print("max:",max)
print("min:",min)
