a  = int(input())
b = [a]
while a != 0:
    a=int(input())
    if a != 0:
        b.append(a)
c = []
if len(b)%2==0:
    for i in range(len(b)//2):
        c.append(b[i]+b[len(b)-1-i])
else:
    for i in range(len(b)//2):
        c.append(b[i]+b[len(b)-1-i])
    c.append(b[(len(b)//2)])
for i in c:
    print(i, end =" ")


