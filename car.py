from vector import Vector

GRAVITY = Vector(0, -1)

class Car(object):
    def __init__(self, position):
        self.position = position
        self.velocity = Vector(0, 0)

    def update(self, dt, gas, tangent):
        acceleration = gas * tangent + GRAVITY
        self.velocity = self.velocity + acceleration * dt
        self.position = self.position + self.velocity * dt
