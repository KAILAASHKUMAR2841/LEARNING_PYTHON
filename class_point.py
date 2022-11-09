class Point:
    def move(self):
        print("MOVE")
    def draw(self):
        print("DRAW")
point1 = Point()
point1.draw()
point1.move()
point1.x = 10
point1.y = 20
print(point1.x)
point2 = Point()
point2.x = 1
point2.y = 2
print(point2.y)

