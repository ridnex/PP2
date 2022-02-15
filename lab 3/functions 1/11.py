from operator import truediv


a = input()

def polindrom(a: str):
    s = str("")
    for i in range(len(a)-1,-1 ,-1):
        s=str(s)+str(a[i])
    if s==a:
        return True
    else:
        return False


print(polindrom(a))

