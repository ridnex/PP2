#Write a Python program to split a string at uppercase letters.

import re

with open("eight.txt", 'r') as f:
    content = f.read()

patern = r'[A-Z]'

x = re.split(patern, content)
print(x)