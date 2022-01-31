a = int(input())
for i in range(a):
    b = str(input())
    if(b.count("@gmail.com")==1):
        s = str()
        for i in range(0,len(b)-10):
            s=s+b[i]
        print(s)
    


    