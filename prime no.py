#generator to generate the prime number 
def prime(x,y):
    for i in range(x,y):
        if i>1:
            for j in range(2,i):
                if(i%j)==0:
                    break
            else:
                yield i
print(list(prime(2,12)))