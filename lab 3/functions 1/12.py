a =[int(i) for i in input().split()]

def histogram(x):
    s = str("")
    for i in range(x):
        s=s+"*"
    return(s)

b = list(map(histogram, a))
for i in b:
    print(i)
