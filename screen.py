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

    def set_window(self, min_x, max_x, curve_data):
        min_y = curve_data.value_at_x(min_x)
        max_y = curve_data.value_at_x(max_x)

        self.__window_min_x = min_x
        self.__window_max_x = max_x
        self.__window_min_y = min_y
        self.__window_max_y = max_y

    def draw_background(self, curve_data):
        curve = curve_data.data_from_to(
            self.__window_min_x, self.__window_max_x)

        points = []
        for p in curve:
            range_x = self.__window_max_x - self.__window_min_x
            range_y = self.__window_max_y - self.__window_min_y
            x = (p[0] - self.__window_min_x ) / range_x * self.__width
            y = (p[1] - self.__window_min_y ) / range_y * self.__height

            points.append((x, y))

        #lines(Surface, color, closed, pointlist, width=1)
        pygame.draw.lines(self.__surface, (255, 0, 0), False, points)

    def draw_car(self, car):
        pass



