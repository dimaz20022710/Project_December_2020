from pygame.draw import *


class Unit:
    """
    This class describes units
    """

    def __init__(self, hp, damage, movement, x, y):
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

    def __init__(self, hp, damage, movement, x, y):
        """
        This function will set the initial characteristics of an object of this class
        :param hp: Unit's health
        :param damage: Unit's damage
        :param movement: Unit's speed
        :param x: Unit's coordinate x
        :param y: Unit's coordinate y
        """
        super().__init__(hp, damage, movement, x, y)

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

    def __init__(self, hp, damage, movement, x, y):
        """
        This function will set the initial characteristics of an object of this class
        :param hp: Unit's health
        :param damage: Unit's damage
        :param movement: Unit's speed
        :param x: Unit's coordinate x
        :param y: Unit's coordinate y
        """
        super().__init__(hp, damage, movement, x, y)

    def hit(self):
        """
        This function describes unit attacks
        """

    def special_ability(self):
        """
        This function describes the superpowers of individual units.
        """


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
        rect(self.screen, (0, 0, 0), (self.x, self.y), ())


class MainMenu:
    """ This is the class responsible for the main menu """
    hovered = False
    clicked = False

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
        self.draw()

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

    def new_window(self):
        """ This function creates a new window """
        color_blue = (159, 182, 205)
        if self.clicked:
            self.screen.fill(color_blue)
        else:
            pass


class Game:
    """ This class is responsible for the game process """

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

    def start_game(self):
        """ This function starts the game """
        color_white = (255, 255, 255)
        self.screen.fill(color_white)
        self.create_new_level()
        self.draw_level()

    def pause_game(self):
        """ The function is responsible for pause during the game """

    def end_game(self):
        """ The function is responsible for the end of the game """

    def reset_game(self):
        """ This function restarts the game """

    def create_new_level(self):
        """ This function creates a new level """

    def next_turn(self):
        """

        :return:
        """

    def next_round(self):
        """

        :return:
        """

    def draw_level(self):
        """

        :return:
        """
        self.draw_field()

    def set_allies(self):
        """

        :return:
        """

    def set_enemies(self):
        """

        :return:
        """
    class Field:
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
                    #def move_unit
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
