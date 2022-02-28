

#Create a generator that generates the squares of numbers up to some number N.
#by iterator:
'''
class Squere:
    def __init__(self, limit):
        self.limit= limit
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a**2 <= self.limit:
            x = self.a**2
            self.a += 1
            return x
        else:
            raise StopIteration
limit = int(input())
myclass = Squere(limit)
myiter = iter(myclass)

for x in myiter:
  print(x)
'''

#by generator

def square_gen(limit):
    i = 1
    while(i**2<= limit):
        x= i **2
        yield x
        i = i + 1


limit = int(input())
for iter in square_gen(limit):
    print(iter)