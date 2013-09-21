import pygame

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
entities = [(AI(), Car(car_start)) for i in range(1)]

screen = Screen(1024, 768)

run = True

def update(dt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                stop()

    car_min_x = len(curve_data)-1
    car_max_x = 0
    car_max_y = entities[0][1].position.y if len(entities) > 0 else 0

    # Update and collect min and max x for determining the draw window.
    for a, c in entities:
        # Fetch curve data.
        curve = curve_data.range(0, c.position.x)  # x == t ?
        curve_p = curve_data.range_p(0, c.position.x)
        # Update AI.
        acceleration = a.update(dt, c, curve, curve_p)
        # Update car.
        graph_level = curve_data.value_at_x(c.position.x)
        height = c.position.y - graph_level
        tangent = Vector(1, curve[-1] - curve[-2]).normalized()
        c.update(dt, height, acceleration, tangent)
        graph_level = curve_data.value_at_x(c.position.x)
        c.position = Vector(
            c.position.x, max(graph_level, c.position.y) + 0.001)

        car_min_x = min(car_min_x, c.position.x)
        car_max_x = max(car_max_x, c.position.x)
        car_max_y = max(car_max_y, c.position.y)

    # Set the window and draw the background.
    screen.set_window(car_min_x, car_max_x, car_max_y, curve_data)
    screen.draw_background(curve_data)

    # Draw all cars.
    for _, c in entities:
        screen.draw_car(c)

    pygame.display.flip()

def main_loop():
    while run:
        update(0.01)

    print "Main loop finished."

def stop():
    global run
    run = False

def main():
    try:
        main_loop()
    except KeyboardInterrupt:
        stop()

if __name__ == "__main__":
    main()
