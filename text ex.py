#program that extracts information from a given text,
#  such as phone numbers, email addresses, and URLs. 
import re
t = "email is sent by thakurshubham@gmail.com and in that mail phone no 8979828604 and url is https://www.shubham.com"
l = re.findall("\S+@\S+", t)
p = re.findall("\d+\d",t)
u = re.findall(r'(https://\S+)',t)
print(l,p,u)