# program that replaces certain words in a string with other words, 
# using regular expressions to match specific patterns. 
import re
t = "email is sent by thakurshubham@gmail.com and in that phone no is 8979828604 and url is https://www.shubham.com"
#replacing email with new mail
result1 = re.sub(r"\S+@\S+","shubhamsingh@gmail.com",t,count=1)
#print(result1)
#replacing phone with new phone no
result2 = re.sub(r"\d+\d","9068991462",result1,count=1)
#print(result2)
#replacing url with url
result3 = re.sub(r"(https://\S+)","https://www.google.com",result2,count=1)
#printing final result
print("original string:",t)
print("updated string:",result3)
