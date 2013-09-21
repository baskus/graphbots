import pygame

from ai         import AI
from car        import Car
from curve      import CurveData
from drawable   import Drawable
from screen     import Screen
from vector     import Vector

#curve_data = fetch_curve_data("VOLV-B.ST")
#curve_data = (numpy.random.random((100,2)), numpy.random.random((100,2)))
curve_data = CurveData("VOLV-B.ST")

# Create 100 (AI, Car) pairs.
entities = [(AI(), Car()) for i in range(100)]

screen = Screen(512, 512)

def update(dt):
    car_min_x = curve_data.min_x
    car_max_x = curve_data.max_x

    # Update and collect min and max x for determining the draw window.
    for a, c in entities:
        # Fetch curve data.
        curve = curve_data.range(0, c.position.x)  # x == t ?
        curve_p = curve_data.range_p(0, c.position.x)
        # Update AI.
        gas = a.update(dt, c.position, c.velocity, curve, curve_p)
        # Update car.
        diff = curve[-1] - curve[-2]
        tangent = Vector(diff[0], diff[1]).normalized()
        c.update(dt, gas, tangent)

        car_min_x = min(car_min_x, c.position.x)
        car_max_x = max(car_max_x, c.position.x)

    # Set the window.
    screen.set_window(car_min_x, car_max_x)

    # Draw all cars.
    for _, c in entities:




class Simulation(object):
    def __init__(self):
        self.__run = False

    def main_loop(self):
        self.__run = True
        while self.__run:
            pass

    def stop(self):
        print "Stopping simulation..."
        self.__run = False

def main():
    s = Simulation()

    try:
        s.main_loop()
    except KeyboardInterrupt:
        s.stop()

if __name__ == "__main__":
    main()
