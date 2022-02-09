#my try 51 test bruh
'''
a = [int(i) for i in input().split()]
i=0;
d=bool
if 0 in a:
    while i<len(a):
        if(i>=len(a)-1 or i+a[i]>=len(a)-1):
            d=True
            break

        if(a[i+a[i]]!=0 or i+a[i]>=len(a)-1):
            i=i+a[i]

        else:
           a[i]=a[i]-1
           if(a[i]==0):
               d = False
               break

    if(d==True):
        print(1)
    else:
        print(0)
else:
    print(1)

'''
#  by teacher :
def can_reach_last_index(array):
    pos = 0
    max_reachable_pos = 0
    while pos < len(array):
        if pos > max_reachable_pos:
            return False
        if pos + array[pos] > max_reachable_pos:
            max_reachable_pos = pos + array[pos]
        if max_reachable_pos >= len(array) - 1:
            return True
        pos += 1
a = [int(i) for i in input().split()]
if(can_reach_last_index(a)==True):
    print(1)
else:
    print(0)
