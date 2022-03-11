#Write a Python program to insert spaces between words starting with capital letters.

import re

with open("eight.txt", 'r') as f:
    content = f.read()

patern = r'[A-Z]'

x = re.split(patern, content)
for i in x:
    print(i, end=" ")