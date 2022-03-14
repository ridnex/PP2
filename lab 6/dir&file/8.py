#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os
import shutil
#i will delete file "deleteme_copy.txt" which from 6.py
shutil.copy("deleteme.txt", "deleteme_copy.txt")
if os.path.exists("deleteme_copy.txt"):
    os.remove("deleteme_copy.txt")
    print("deleted")
else:
    print("no such file")