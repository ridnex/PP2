#Write a Python program with builtin function to multiply all the numbers in a list
b = [int(i) for i in input().split()]
#print(b)
tot = 1
for i in range(0,len(b)):
    tot = tot *b[i]
print(tot)

