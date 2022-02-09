a = str(input())
b =[]
boolian = bool
k ='['
k1=']'
t ='('
t1=')'
s='{'
s1='}'
for i in range(len(a)):
    if(a[i]==k or a[i]==t or a[i]==s):
        b.append(a[i])
    elif(a[i]==k1):
        if len(b)==0:
            boolian = False
            break
        elif b[len(b)-1]== k:
            boolian = True
            b.pop()
        else:
            boolian = False
    elif(a[i]==t1):
        if len(b)==0:
            boolian = False
            break
        elif b[len(b)-1]== t:
            boolian = True
            b.pop()
        else:
            boolian = False
    elif(a[i]==s1):
        if len(b)==0:
            boolian = False
            break
        elif b[len(b)-1]== s:
            boolian = True
            b.pop()
        else:
            boolian = False
        
if(len(b)>0):
    boolian = False
if(boolian == True):
    print("Yes")
else:
    print("No")

