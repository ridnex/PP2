a = input()
b = [int(i) for i in a.split()]

def has_33(arr):
    d = 0 
    for i in range(len(arr)-1):
        if(arr[i]==3 and arr[i+1]==3):
            d+=1
            return True
    if d==0:
        return False
    
print(has_33(b))
    
