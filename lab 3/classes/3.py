class Shape():
    def __init__(self):
        self.ari = 0
    def area(self):
        print(self.ari)
  
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)

    def area(self):
        self.ari = self.length * self.width
        super().area()
    
len = int(input())
wid = int(input())
answer = Rectangle(len, wid)
answer.area()