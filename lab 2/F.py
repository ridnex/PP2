a = {}
b = int(input())
c = []
for i in range(b):
    s, d  = map(str, input().split())
    if s in a.keys():
        a[s]=int(a[s]) + int(d)
    else:
        a[s]=int(d)
maxi=0
for i in a.values():
    if(int(i)>=maxi):
        maxi = i
for i in a.keys():
    c.append(i)
c.sort()
for i in c:
    if(int(a[i])==maxi):
        print(str(i)+" is lucky!")
    else:   
        print(str(i)+" has to receive", maxi-int(a[i]), "tenge")

    






