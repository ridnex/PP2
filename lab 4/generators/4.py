# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.


#by iterator:
'''
class Square_a_b:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        self.x = self.start
        return self
    def __next__(self):
        if(self.x <= self.end):
            square = self.x ** 2
            self.x = self.x + 1 
            return square
        else:
            raise StopIteration 

a, b = map(int, input().split())
myclass = Square_a_b(a, b)
myiter = iter(myclass)
for item in myiter:
    print(item)
'''

#by gen
def square_a_b(start, end):
    for i in range(start, end+1, ):
        yield i**2
a, b = map(int, input().split())
for item in square_a_b(a, b):
    print(item)