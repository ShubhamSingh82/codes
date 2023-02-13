#program to read a json file and print it.
import json
x = open("xyz.json")
data = json.load(x)
print(data)
x.close()