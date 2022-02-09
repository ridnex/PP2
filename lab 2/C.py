n = int(input())
array = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i==0 or j==0:
            array[i][j]=i+j
        elif i==j:
            array[i][j]=i*j
        else:
            array[i][j]=0

for i in range(n):
    for j in range(n):
        print(array[i][j],end=' ')
    print()
