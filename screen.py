import pygame

class Screen(object):
    def __init__(self, width, height):
        self.__surface = pygame.display.set_mode((width, height))

        self.__width = width
        self.__height = height

        self.__window_min_x = None
        self.__window_max_x = None
        self.__window_min_y = None
        self.__window_max_y = None

    def set_window(self, min_x, max_x, min_y, max_y, curve_data):

        zoom=100
        if max_x - min_x < zoom:
            temp = (max_x + min_x)/2.0
            max_x = temp + zoom/2.0
            min_x = temp - zoom/2.0

        min_x_y = curve_data.value_at_x(min_x)
        max_x_y = curve_data.value_at_x(max_x)

        min_y = min(min_x_y, max_x_y, min_y)
        max_y = max(min_x_y, max_x_y, max_y)

        max_rx_ry=max(max_x-min_x,max_y-min_y)

        if max_x-min_x<max_y-min_y:
            temp = (max_x+min_x)/2.0
            max_x=temp+max_rx_ry/2.0
            min_x=temp-max_rx_ry/2.0
        else:
            temp = (max_y+min_y)/2.0
            max_y=temp+max_rx_ry/2.0
            min_y=temp-max_rx_ry/2.0

        self.__window_min_x = min_x
        self.__window_max_x = max_x
        self.__window_min_y = min_y
        self.__window_max_y = max_y

        print max_x - min_x

    def draw_background(self, curve_data):
        self.__surface.fill((255,255,255))

        min_i = max(0, int(self.__window_min_x) - 1)
        max_i = int(self.__window_max_x) + 2
        curve = curve_data.range(min_i, max_i)


        points = []
        range_x = float(self.__window_max_x - self.__window_min_x)
        range_y = float(self.__window_max_y - self.__window_min_y)
        for i in range(len(curve)):

            x = (float(min_i + i) - self.__window_min_x) / range_x

            #x = float(min_i + i) / len(curve)
            y = 1.0 - (curve[i] - self.__window_min_y) / range_y

            points.append((int(x* self.__width), int(y * self.__height)))

        # lines(Surface, color, closed, pointlist, width=1)
        pygame.draw.lines(self.__surface, (255, 0, 0), False, points)

    def draw_car(self, car):
        range_x = float(self.__window_max_x - self.__window_min_x)
        range_y = float(self.__window_max_y - self.__window_min_y)

        x = (car.position.x - self.__window_min_x) / range_x * self.__width
        y = (1.0 - (car.position.y - self.__window_min_y) / range_y) \
            * self.__height

        color = (0, 0, 255) if car.alive else (255, 0, 0)

        # circle(Surface, color, pos, radius, width=0) -> Rect
        pygame.draw.circle(self.__surface, color, (int(x), int(y)), 5)
