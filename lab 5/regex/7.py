#Write a python program to convert snake case string to camel case string.
#it is work only for snakes with lens 2 a_b
import re

with open("snake.txt", 'r') as f:
    content = f.read()

snake = r"([a-z]+)_([a-z])([a-z]*)"

x = re.finditer(snake, content)
for i in x:
    print(i.group(1)+i.group(2).upper()+i.group(3))
