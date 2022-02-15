
import myfunction

b=int(input())
#1.py
t = myfunction.convert_g(b)
print(t)
#2.py
s= myfunction.convert_gradus(float(b))
print(s)
#3.py
num_legs = int(input())
num_heads = int(input())
myfunction.solve(num_legs,num_heads )

#4.py
a = input()
b = [int(i) for i in a.split()]

print(list(filter(myfunction.prime, b)))

#e.t.c
#all my functions in myfunction.py
'''
by using this i can call any fucntions from this file 
also every my functions name are not same
'''