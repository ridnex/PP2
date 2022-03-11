#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
#for any txt file :

import re

with open("note.txt", "r") as f:
    content = f.read()

x = re.finditer(r'ab{2,3}', content)
for i in x:
    print(i.group())

#for input
'''
import re
content = str(input())
x = re.findall(r'ab{2,3}', content)
print(x)
'''