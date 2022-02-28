#Implement a generator that returns all numbers from (n) down to 0.

#by ierator:
'''
class Back:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.x=self.start
        return self
    
    def __next__(self):
        if(self.x>=0):
            self.y = self.x
            self.x = self.x -1
            return self.y
        else:
            raise StopIteration

start = int(input())
myclass = Back(start)
myiter = iter(myclass)

for i in myiter:
    print(i)
'''

# by generator:
def back_gen(start):
    for i in range(start, -1, -1):
        yield i
start = int(input())
for item in back_gen(start):
    print(item)