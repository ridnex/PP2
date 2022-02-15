a = input()
b =[str(i) for i in a.split()]

def reverse_arr_of_str(arr):
    for i in range(len(arr)//2):
        k = arr[i]
        arr[i]=arr[len(arr)-1-i]
        arr[len(arr)-1-i]=k

    return arr

reversed_arr = reverse_arr_of_str(b)
for i in reversed_arr:
    print(i, end=" ")
