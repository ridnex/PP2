a = int(input())
b = [int(a) for a in input().split(" ", a-1)]
b.sort(reverse = True)
print(b[0]*b[1])