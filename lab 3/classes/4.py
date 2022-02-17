import math

class Point():
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    
    def show(self):
        print(f'x coordinate: {self.x_coordinate} and y coordinate: {self.y_coordinate} ')

    def move( self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def dist(self, x_coordinate : int, y_coordinate : int):
        distanse = math.sqrt((x_coordinate-self.x_coordinate)**2 + (y_coordinate-self.y_coordinate)**2)
        print(float(distanse))
#1
x_coor = int(input())
y_coor = int(input())

points = Point(x_coor, y_coor)
points.show()

#2
x1_coor = int(input())
y1_coor = int(input())
points = Point(x1_coor, y1_coor)
points.show()

#3
x3_coor = int(input())
y3_coor = int(input())
points.dist(x3_coor, y3_coor)


