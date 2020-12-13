from pygame.draw import rect
from random import randint as rint


class Wall:
    """
    This class of walls that will be painted on the field
    """

    def __init__(self, screen, x, y, height, width):
        """
        This function will set the initial characteristics of an object of this class
        :param screen: The screen on which the object of this class is drawn
        :param x: The coordinate x of an object of this class
        :param y: The coordinate y of an object of this class
        :param height: Height of an object of this class
        :param width: Width of an object of this class
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw_wall(self):
        """ This function draws the wall """
        rect(self.screen, (0, 0, 0), (self.x, self.y, self.height, self.width))


class Field:
    hovered = False
    clicked = False

    def __init__(self, screen, screen_height, screen_width, N):
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
        self.walls = []
        self.walls_1 = []
        self.cell_size = screen_height // (N + 1)
        self.cells = []

    def draw_map(self):
        for i in range(self.N + 1):
            self.cells.append([])
            for j in range(1, self.N):
                rect(self.screen, (0, 0, 0), (i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size),
                     2)
                self.cells[i].append([i * self.cell_size, j * self.cell_size, 0])
        self.draw_walls()
        return self.cells

    def draw_walls(self):
        walls = []
        walls_1 = []
        for i in range(rint(self.N // 4, self.N // 3)):
            walls.append(Wall(self.screen, rint(1, self.N - 3) * self.cell_size,
                              rint(3, self.N // 2 - 2) * self.cell_size,
                              rint(1, self.N // 4) * self.cell_size,
                              rint(1, self.N // 4) * self.cell_size))
            for j in range(walls[i].height // self.cell_size):
                for k in range(walls[i].width // self.cell_size):
                    self.cells[walls[i].x // self.cell_size + j][
                        walls[i].y // self.cell_size + k - 1][2] = -1

        ind = 0
        for i in walls:
            walls_1.append(Wall(self.screen, i.x, self.screen_width - i.y - i.width, i.height, i.width))
            for j in range(walls_1[ind].height // self.cell_size):
                for k in range(walls_1[ind].width // self.cell_size):
                    self.cells[walls_1[ind].x // self.cell_size + j][
                        walls_1[ind].y // self.cell_size + k - 1][2] = -1
            ind += 1
        self.walls = walls
        self.walls_1 = walls_1
        for i in self.walls:
            i.draw_wall()
        for i in self.walls_1:
            i.draw_wall()


class Bar:
    """

    """

    hovered = 0
    clicked = 0

    def __init__(self, text, pos, screen, menu_font):
        """
        This function sets the initial conditions for an object from this class
        :param text: Text to be written
        :param pos: Positioning text on screen
        :param screen: Screen on which text is displayed
        :param menu_font: Text font
        """
        self.text = text
        self.pos = pos
        self.screen = screen
        self.menu_font = menu_font
        self.set_rect()

    def draw(self):
        """ This function draws a menu screen """
        self.set_rend()
        self.screen.blit(self.rend, self.rect)

    def set_rend(self):
        """ This function renders the menu """
        self.rend = self.menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        """ This function changes the color of the button in the menu """
        color_red = (255, 0, 0)
        color_white = (255, 255, 255)
        color_gray = (100, 100, 100)

        if self.hovered:
            if self.clicked:
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


import math
def check_walls(unit, aim, cell_size, cells):
    K = 100
    points = []
    dy = (aim.y - unit.y) / K
    dx = (aim.x - unit.x) / K
    for i in range(K):
        points.append([unit.x + math.ceil(i * dx), unit.y + math.ceil(i * dy)])
        #points.append([unit.x + math.ceil(i * dx), unit.y + math.ceil(i * dy)])
    for i in cells:
        for j in i:
            for k in points:
                if (k[0] - j[0] > 0) and (k[0] - j[0] < cell_size) and (k[1] - j[1] > 0) and (
                        k[1] - j[1] < cell_size):
                    if j[2] == -1:
                        return 1
    return 0