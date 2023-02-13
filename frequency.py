#program to count the frequency of each element in a list and store it in a dictionary. 
def count_words(list):
    count = dict()
    
    for i in list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
x = count_words(["a","b","c","a"])
print(x)