a, b = map(int, input().split())
c= 0
for i in range(1,a+1):
    if a%i==0:
        c=c+1

if(c==2 and a<=500 and b%2==0):
    print("Good job!")
else:
    print("Try next time!")