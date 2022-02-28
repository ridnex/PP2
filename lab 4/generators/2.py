#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

#by iterator
'''
class Even:
    def __init__(self, limit):
        self.limit = limit
    
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        if self.num <= self.limit:
            x = self.num
            self.num = self.num +1
            return x
            
        else:
            raise StopIteration

limit = int(input())   
myclass = Even(limit)  
myiter = iter(myclass)
for i in myiter:
    if i%2==0:
        if i == limit or i==limit-1:
            print(i)
        else:
            print(i, end =",")
'''
#by generator

def even_gen(limit):
    i = 1
    while(i <= limit):
        if i%2 == 0:
            yield i;
        i = i + 1
limit = int(input())
for item in even_gen(limit):
    if(item == limit or item == limit -1):
        print(item)
    else:
        print(item, end=', ')
