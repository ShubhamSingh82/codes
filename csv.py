#program to perform operations on a CSV file,
#such as reading from a CSV file and writing to a CSV file. 
import csv
#reading from a csv file
with open("update.csv",'r') as file1:
    reader = csv.reader(file1)
    for i in reader:
        print(i)

#writing in csv file
i = [["name","age","company"],
     ["shubham",24,"mindtree"],
     ["ravi",27,"infosys"]]
with open("update.csv",'w',newline='') as file2:
    writer = csv.writer(file2)
    writer.writerows(i)
