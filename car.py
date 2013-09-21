from vector import Vector

GRAVITY = Vector(0, -10)

class Car(object):
    def __init__(self, position):
        self.position = position
        self.velocity = Vector(0, 0)
        self.alive = True

    def update(self, dt, height, acceleration, tangent):
        drag = -self.velocity.normalized() if self.velocity.length() > 0 else \
            Vector(0, 0)
        if height > 0:
            acc = tangent * acceleration + tangent * GRAVITY.dot(tangent) \
                - drag
        else:
            acc = GRAVITY - drag
        velocity_old = self.velocity
        self.velocity = self.velocity + acc * dt

        # Check death.
        impulse = (velocity_old - self.velocity).length()
        print "impulse:", impulse
        if impulse > 150:
            print "DIE!"
            self.alive = False

        self.position = self.position + self.velocity * dt
