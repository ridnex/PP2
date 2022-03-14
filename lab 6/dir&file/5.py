#Write a Python program to write a list to a file.
list = ["one", "two", "three", "four", "five", "six"]
with open("txt.txt", "w") as f:
    for item in list:
        f.write(f"{item}\n" )


