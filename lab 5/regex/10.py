#Write a Python program to convert a given camel case string to snake case.
#it is work only for 2 (asd)(H)(csdc)->asd_hcsdc
import re

with open("camel.txt", 'r') as f:
    content = f.read()

camel = r'([a-z]+)([A-Z])([a-z]*)'

x = re.finditer(camel, content)
for i in x:
    print(i.group(1)+"_"+i.group(2).lower()+i.group(3))
