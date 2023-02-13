#program to take the inputs from the user and add into json file.  
import json
x = {
    "name":"shubham",
    "age" : 24,
    "city" : "mathura"
}
with open("xyz.json",'w') as file1:
    json.dump(x,file1)
  