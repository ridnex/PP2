b = [int(a) for a in input().split(" ")]
if(len(b)==1):
    n=b[0]
    x = int(input())
else:
    n=b[0]
    x=b[1]
arr = []
for i in range(n):
    d= x + (2*i)
    arr.append(d)
d = 0
for i in arr:
    d = d ^ i
print(d)  