#Write a Python program that invoke square root function after specific milliseconds. 
import time
integer = int(input())
milis = int(input())
time.sleep(milis/1000)
print(pow(integer, 1/2))
#pow builtin f


