import math
a = int(input())
b = str(input())
d = float()
c = int()
if b=="k":
    c = int(input())
    d = a / 1024
    print(round(d, c))
else:
    print(a*1024)