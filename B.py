a =input()
b = 0
for i in range(len(a)):
    b = b + ord(a[i])
if(b>300):
    print("It is tasty!")
else:
    print("Oh, no!")

