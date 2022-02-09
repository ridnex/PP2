a = str(input())
a1=a.replace("!","")
a2=a1.replace(",","")
a3=a2.replace("?","")
a4=a3.replace(".","")

c ={str(i) for i in a4.split()}
b= []
for j in c:
    b.append(j)
b.sort()
print(len(b))
for i in b:
    print(i)
    