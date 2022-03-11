#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.


import re

with open("note.txt", 'r') as f:
    content = f.read()

pattern = r"a.+b"
x = re.finditer(pattern, content)
for i in x:
    print(i.group())