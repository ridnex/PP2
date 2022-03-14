#Write a/Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

upper = 0
lower =0
a = str(input())
#isupper islower builtin functions
for i in a:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print(f"upper: {upper} --- lower: {lower}")

