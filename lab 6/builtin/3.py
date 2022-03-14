#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
a = str(input())
c = "".join(reversed(a))
if a == c:
    print("T")
else:
    print("F")

#reversed = bultin f