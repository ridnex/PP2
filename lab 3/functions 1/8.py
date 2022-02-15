
a = input()
b = [int(i) for i in a.split()]

def has_007(arr: list):
    c= ""
    for i in range(len(arr)):
        if arr[i]==7 or arr[i]==0:
            c = str(c) + str(arr[i])

    if "007" in c:
        return True
    else:
        return False

print(has_007(b))


