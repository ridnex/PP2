#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os
paths = os.getcwd()  
path_file = os.path.join(paths, "deleteme.txt" )
if os.path.exists(path_file):
    os.remove(os.path.basename(path_file))
    print("deleted")
else:
    print("no such file")