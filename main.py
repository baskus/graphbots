from ai         import AI
from car        import Car
from curve      import CurveData
from screen     import Screen
from vector     import Vector

#curve_data = fetch_curve_data("VOLV-B.ST")
#curve_data = (numpy.random.random((100,2)), numpy.random.random((100,2)))
curve_data = CurveData("VOLV-B.ST")

# Create 100 (AI, Car) pairs.
car_start = Vector(10, curve_data.value_at_x(10))
entities = [(AI(), Car(car_start)) for i in range(100)]

screen = Screen(512, 512)

run = True

def update(dt):
    car_min_x = curve_data.min_x
    car_max_x = curve_data.max_x

    # Update and collect min and max x for determining the draw window.
    for a, c in entities:
        # Fetch curve data.
        curve = curve_data.range(0, c.position.x)  # x == t ?
        curve_p = curve_data.range_p(0, c.position.x)
        # Update AI.
        acceleration = a.update(dt, c, curve, curve_p)
        # Update car.
        graph_level = curve.value_at_x(c.position.y)
        c.position = Vector(c.position.x, max(graph_level, c.position.y))
        height = c.position.y - graph_level
        diff = curve[-1] - curve[-2]
        tangent = Vector(diff[0], diff[1]).normalized()
        c.update(dt, height, acceleration, tangent)

        car_min_x = min(car_min_x, c.position.x)
        car_max_x = max(car_max_x, c.position.x)

    # Set the window and draw the background.
    screen.set_window(car_min_x, car_max_x)
    screen.draw_background(curve_data)

    # Draw all cars.
    for _, c in entities:
        screen.draw_car(c)

def main_loop():
    while run:
        update(0.5)

    print "Main loop finished."

def stop():
    run = False

def main():
    try:
        main_loop()
    except KeyboardInterrupt:
        stop()

if __name__ == "__main__":
    main()
