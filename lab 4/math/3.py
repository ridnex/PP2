# Write a Python program to calculate the area of regular polygon.

import math
# I would like to find area by parts(there n sides regular polygon than n part of triangle)
number_sides = int(input())
length = int(input())
gradus = (2*math.pi)/number_sides
#gradus triangle 360/n but in radian 
hight = (1/math.tan(gradus/2)) * (length/2)
#by 1/tan it is ctg I find hight of little triangle
area = (hight * length)/2 * number_sides

print(round(area))
#i used round to be sure because sometimes sin(30 gradus) give output 0.49999999999
