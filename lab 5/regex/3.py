#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

with open("note.txt", 'r') as f:
    content = f.read()

pattern = r"[a-z]+_[a-z]+"
x = re.finditer(pattern, content)
for i in x:
    print(i.group())