
a = str(input())
k=0
n=0
for i in range(len(a)-1,-1,-1):
    n = n + int(a[i])*(2**k)
    k = k + 1
print(n)

'''
a = str(input())
def recoursion(a, k, i):
    if(i==0):
        return (int(a[0])*(2**k))
    else:
        int(a[i])*(2**k) + recoursion(a, k+1, i-1)

print(recoursion(a, 0, len(a)-1))
'''
    