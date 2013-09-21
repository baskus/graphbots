class AI(object):
    def __init__(self):
        pass

    def update(self, dt, position, velocity, curve, curve_p):
        """Calculate the amount of gas"""
        height = position.y - curve.value_at_x(position.x)

        # Always accelerate for now.
        return 1.0
