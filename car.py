from vector import Vector

GRAVITY = Vector(0, -10)

class Car(object):
    def __init__(self, position):
        self.position = position
        self.velocity = Vector(0, 0)

    def update(self, dt, height, acceleration, tangent):
        if height > 0:
            acc = tangent * acceleration + tangent * GRAVITY.dot(tangent)
        else:
            acc = GRAVITY
        self.velocity = self.velocity + acc * dt
        self.position = self.position + self.velocity * dt
