a =input().split()

def uniq(arr: list):
    new_arr= []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr

print(uniq(a))