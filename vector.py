import math

class Vector(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)

    def __repr__(self):
        return "Vector(%f, %f)" % (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self, other):
        return Vector(-self.x, -self.y)

    def length(self):
        return math.sqrt(self.x**2.0 + self.y**2.0)

    def normalized(self):
        L = self.length()
        return Vector(self.x / L, self.y / L)

    def dot(self, other):
        return self.x * other.x + self.y * other.y
