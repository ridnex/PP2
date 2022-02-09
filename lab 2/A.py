a = [int(i) for i in input().split()]
i=0;
d=bool
if 0 in a:
    while i<len(a):
        if(i>=len(a)-1 or i+a[i]>=len(a)-1):
            d=True
            break

        if(a[i+a[i]]!=0 or i+a[i]>=len(a)-1):
            i=i+a[i]

        else:
           a[i]=a[i]-1
           if(a[i]==0):
               d = False
               break

    if(d==True):
        print(1)
    else:
        print(0)
else:
    print(1)

