a = str(input())
b = []
s = str()
answer = str()
for i in range(len(a)):
    if(a[i]!=" "):
        s = s + a[i]
    else:
        b.append(s)
        s =""
    if(i==len(a)-1):
        b.append(s)
for i in range(len(b)):
    t = b[i]
    if(len(t)>=3):
        answer = answer + t +" "
print(answer)


