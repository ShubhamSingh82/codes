# program to read the contents of a text file. 
x = input("enter the name of text file")
file1 = open(x,'r')
content = file1.read()
print(content)