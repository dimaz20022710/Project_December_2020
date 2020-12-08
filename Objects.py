from pygame.draw import rect, line
from random import randint as rint

'''
class Unit(ABC):
    """
    This class describes units
    """

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size):
        """
        This function will set the initial characteristics of an object of this class
        :param hp: Unit's health
        :param damage:Unit's damage
        :param movement: Unit's speed
        :param x: Unit's coordinate x
        :param y:Unit's coordinate y
        """
        self.hp = hp
        self.damage = damage
        self.movement = movement
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.clicked = False
        self.side = side
        self.screen = screen
        self.cell_size = cell_size

    @abstractmethod
    def draw_unit(self):
        """
        This function draws a unit
        """

    def move_unit(self):
        """
        This function describes the movement of the unit
        """


class MeleeUnit(Unit):
    """
    A subclass of units that use melee combat
    """

    def draw_unit(self):
        if self.side == 1:
            rect(self.screen, (0, 255, 0), (self.x, self.y, self.cell_size, self.cell_size))
        else:
            rect(self.screen, (255, 0, 0), (self.x, self.y, self.cell_size, self.cell_size))

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size):
        """
        This function will set the initial characteristics of an object of this class
        :param hp: Unit's health
        :param damage: Unit's damage
        :param movement: Unit's speed
        :param x: Unit's coordinate x
        :param y: Unit's coordinate y
        """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size)

    def hit(self):
        """
        This function describes unit attacks
        """

    def special_ability(self):
        """
        This function describes the superpowers of individual units.
        """


class RangeUnit(Unit):
    """
    A subclass of units that use range combat
    """

    def draw_unit(self):
        if self.side == 1:
            rect(self.screen, (0, 105, 0), (self.x, self.y, self.cell_size, self.cell_size))
        else:
            rect(self.screen, (105, 0, 0), (self.x, self.y, self.cell_size, self.cell_size))

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size):
        """
        This function will set the initial characteristics of an object of this class
        :param hp: Unit's health
        :param damage: Unit's damage
        :param movement: Unit's speed
        :param x: Unit's coordinate x
        :param y: Unit's coordinate y
        """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size)

    def hit(self):
        """
        This function describes unit attacks
        """

    def special_ability(self):
        """
        This function describes the superpowers of individual units.
        """
'''

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

    def draw_level(self):
        walls = []
        walls_1 = []
        for i in range(rint(self.N // 4, self.N // 3)):
            walls.append(Wall(self.screen, rint(1, self.N - 3) * (self.screen_height // (self.N + 1)),
                              rint(3, self.N // 2 - 2) * (self.screen_height // (self.N + 1)),
                              rint(1, self.N // 3) * (self.screen_height // (self.N + 1)),
                              rint(1, self.N // 3) * (self.screen_height // (self.N + 1))))
        for i in walls:
            walls_1.append(Wall(self.screen, i.x, self.screen_width - i.y - i.width, i.height, i.width))
        self.walls = walls
        self.walls_1 = walls_1
        for i in self.walls:
            i.draw_wall()
        for i in self.walls_1:
            i.draw_wall()

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
