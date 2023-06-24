import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.center = Point(x, y)
        self.radius = radius

    def contains(self, point):
        distance = math.sqrt((point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2)
        return distance <= self.radius

