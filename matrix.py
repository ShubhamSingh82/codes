#program to perform operations on a matrix, such as adding two matrices,
#multiplying two matrices, and transposing a matrix using nested loops. 
x =[[1,2,3],
    [4,5,6],
    [7,8,9]]
y =[[11,12,13],
    [14,15,16],
    [17,18,19]]
z =[[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        z[i][j] = x[i][j] + y[i][j]
print("the addition of two matrix:")
for l in z:
    print(l)
#multiplying two matrix
for i in range(len(x)):
    for j in range(len(x[0])):
        for k in range(len(y)):
            z[i][j] += x[i][j] * y[i][j]
print("the multiplication of two matrix:")
for l in z:
    print(l)
#transpose of x matrix
for i in range(len(x)):
    for j in range(len(x[0])):
        z[i][j] = x[j][i] 
print("the transpose of  matrix:")
for l in z:
    print(l)