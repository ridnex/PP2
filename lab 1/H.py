a = str(input())
b = input()
if(a.count(b)>=2):
    for i in range(len(a)):
        if(a[i]==b):
            first=i
            break
    for i in range(len(a)-1, -1, -1):
        if(a[i]==b):
            last=i
            break
    print(first, last)
elif(a.count(b)==1):
    for i in range(len(a)):
        if(a[i]==b):
            first=i
            break
    print(first)
