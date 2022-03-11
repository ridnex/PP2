#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

with open("note.txt", 'r') as f:
    content = f.read()

'''
x = re.sub("\s", ":", content)
x = re.sub("\.", ":", x)
x = re.sub(",", ":", x)
'''

#x = re.sub("[\s\.,]", ":", content)
x = re.sub("[ .,]", ":", content)
print(x)