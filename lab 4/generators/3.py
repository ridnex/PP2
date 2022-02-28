#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

#by iterator 
'''
class Divisible:
    def __init__(self, limit):
        self.limit = limit
    def __iter__(self):
        self.a=0
        return self
    def __next__(self):
        if(self.a<=self.limit):
            x = self.a
            self.a = self.a + 1
            return x
                
        else:
            raise StopIteration

limit = int(input())
myclass = Divisible(limit)
myiter = iter(myclass)

for iter in myiter:
    if iter % 3 == 0 and iter %4 == 0:
        print(iter)
'''

# by generator
from re import I


def divisible_gen(limit):
    i = 0
    while(i<=limit):
        if(i%3==0 and i%4==0):
            yield i
        i = i + 1

limit = int(input())
for item in divisible_gen(limit):
    print(item)