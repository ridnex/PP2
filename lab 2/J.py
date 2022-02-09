a = int(input())
b= {""}
c= []
b.clear()

def qwe(s):
    num=0
    upp=0
    low=0
    for i in range(len(str(s))):
        if ord(s[i])<58:
            num+=1
        elif str(s[i])==str(s[i]).upper():
            upp+=1
        elif str(s[i])==str(s[i]).lower():
            low+=1
        
    if upp>0 and low >0 and num>0:
        return True
    else :
        return False
        
for i in range(a):
        a = str(input())
        b.add(a)


for i in b:
    if qwe(i)==True:
        c.append(i)

print(len(c))
c.sort()
for i in c:
    print(i)