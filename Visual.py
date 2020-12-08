from pygame.draw import *


class Field:
    def __init__(self, screen, screen_height, screen_width, N, rend):
        """
        This function is responsible for the initial screen characteristics when creating an object of this class.
        :param screen: The screen that is being created
        :param screen_height:
        :param screen_width:
        :param N:The number of lines vertically and horizontally, respectively
        """
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.N = N

    def draw_field(self):
        """ This function draws a field """
        # Top-left coordinate
        x1 = 0
        y1 = 0
        # Top-right coordinate
        x2 = self.screen_width
        y2 = self.screen_height
        black_color = (0, 0, 0)
        rect(self.screen, black_color, (x1, y1, x2 - x1, y2 - y1), 2)
        h = (x2 - x1) // (self.N + 1)  # Width of one cell
        x = x1 + h
        w = (y2 - y1) // (self.N + 1)  # Height of one cell
        y = y1 + w
        for i in range(self.N):
            """ This loop draws N horizontal and vertical lines """
            line(self.screen, black_color, (x, y1), (x, y2))  # Vertical lines
            x += h
            line(self.screen, black_color, (x1, y), (x2, y))  # Horizontal lines
            y += w

    def set_rend(self):
        """ This function renders the menu """
        self.rend = self.cell_font.render(self.text, True, self.get_color())

    def get_color(self):
        """ This function changes the color of the button in the menu """
        color_red = (255, 0, 0)
        color_white = (255, 255, 255)
        color_gray = (100, 100, 100)

        if self.hovered:
            if self.clicked:
                # def move_unit
                return color_red
            else:
                return color_white
        else:
            return color_gray

    def set_rect(self):
        """ This function is responsible for the interaction of the player with the buttons in the menu. """
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos
