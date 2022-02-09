
a = []
b = input()
while b!="0":
    c = [str(a) for a in b.split()]
    c.reverse()
    a.append(c)
    b = input()
a.sort()
for i in a:
    i = i.reverse()
for i in a:
    k = 0
    for j in i:
        k+=1
        if k==3:
            print(j)
        else:
            print(j, end =" ")
        
    
