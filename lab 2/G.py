a = int(input()) 
diction = {}

for i in range(a):
    c, b = map(str, input().split())
    if b in diction:
        diction[b]=int(diction[b])+1
    else:
        diction[b]=1

k=int(input())
for i in range(k):
    m = [str(a) for a in input().split(" ")]
    if m[1] in diction:
        diction[m[1]]=int(diction[m[1]])-int(m[2])
demon = 0
for i in diction.values():
    if int(i) > 0 :
        demon=demon+int(i)
print("Demons left:", demon)
    


