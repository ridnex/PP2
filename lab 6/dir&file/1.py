#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

os.chdir('../')    #one step back from dir(path)
#I would like to find all falders and files in file lab 6
paths = os.getcwd()  #now path
#paths = input()
print("only DIR: ")
for item in os.listdir(paths):
    target_path = os.path.join(paths , item)
    if os.path.isdir(target_path):
        print(f'Dir : {item}')

print("only File:")
for item in os.listdir(paths):
    target_path = os.path.join(paths , item)
    if os.path.isfile(target_path):
        print(f'File : {item}')

print("all:")
for item in os.listdir(paths):
   print(item)