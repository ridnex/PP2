# Write a Python program to convert degree to radian.
import math
degree = int(input())
radian = float(degree * (math.pi/180))
print(radian)
print(round(radian, 6))