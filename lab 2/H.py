import math
a, b = map(int, input().split())
c = int(input())
w = {}
d = []
for i in range(c):
    x, y = map(int, input().split())
    n=str(x)+" "+str(y)
    w[n]=math.sqrt((a-x)**2+(b-y)**2)
    d.append(math.sqrt((a-x)**2+(b-y)**2))
d.sort()
for i in d:
    for j in w.keys():
        if i==w[j]:
            print(j)
            



