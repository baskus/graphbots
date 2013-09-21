class AI(object):
    def __init__(self):
        pass

    def update(self, dt, position, velocity, curve_data, curve_p):
        """Calculate the amount of gas"""
        #height = position.y - curve.value_at_x(position.x)

        # Always accelerate for now.
        import random
        return 4.0 * random.random()
