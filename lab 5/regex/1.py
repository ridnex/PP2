#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
#for any txt file :

import re

with open("note.txt", 'r') as f:
    contents = f.read()

a = re.finditer(r'ab*', contents)
for res in a:
    print(res.group())
    
'''
#for just input
import re
contents = str(input())
a = re.findall(r'ab*', contents)
print(a)
'''