#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

with open("note.txt", 'r') as f:
    content = f.read()

pattern = r"[A-Z][a-z]+"
x = re.finditer(pattern, content)
for i in x:
    print(i.group())