#Write a Python program to convert a given camel case string to snake case.

import re

with open("eight.txt", 'r') as f:
    content = f.read()

patern = r'[A-Z]'
str = ""
x = re.split(patern, content)
for i in x:
    str = str+"_"+i
print(str)