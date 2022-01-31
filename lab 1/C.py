a = input()
b = str()
for i in range(len(a)):
    if ord(a[i])>=65 and ord(a[i])<=90:
        b = b + chr(ord(a[i])+32)
    else:
        b = b + a[i]
print(b)
