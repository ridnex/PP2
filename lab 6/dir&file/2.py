#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os
path = os.getcwd()
file_name = input()
path_file = os.path.join(path, file_name)



print(f"exitence: {os.access(path_file, os.F_OK)}")
print(f"readability: {os.access(path_file, os.R_OK)}")
print(f"writability: {os.access(path_file, os.W_OK)}")
print(f"executability: {os.access(path_file, os.X_OK)}")