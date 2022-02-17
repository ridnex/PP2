class Shape():
    def __init__(self):
        self.ari = 0
    def area(self):
        print(self.ari)
    



class Square(Shape):
    def __init__(self, lenth : int):
        self.lenth = lenth

    def area(self):
        self.ari = self.lenth ** 2
        super().area()


len = int(input())
a = Square(len)
a.area()
