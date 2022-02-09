a = []
n = int(input())
string = ""
for i in range(n):
    x= input()
    if len(x)==1:
        if len(a)!=0:
            string = string + a[0]+" "
            a.pop(0)
    else:
        r, t =map(str, x.split())
        a.append(t)
print(string)
