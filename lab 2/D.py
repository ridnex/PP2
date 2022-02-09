n = int(input())
array = [['.' for i in range(n)] for j in range(n)]
if n%2==1:
    for i in range(n):
        for j in range(n):
            if(j+i>=n-1):
                array[i][j]="#"
else:
    for i in range(n):
        for j in range(n):
            if(i-j>=0):
                array[i][j]="#"
for i in range(n):
    for j in range(n):
        print(array[i][j],end='')
    print()
