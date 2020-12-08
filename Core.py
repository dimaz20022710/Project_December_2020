from Objects import Wall, Field
from random import randint as rint
from Units import MeleeUnit, RangeUnit


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

        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen = screen
        self.N = N
        self.cell_size = (self.screen_height // (self.N + 1))
        self.melee_number = 0
        self.ranged_number = 0
        self.units_1 = []
        self.units_2 = []

    def start_game(self):
        """ This function starts the game """
        color_white = (255, 255, 255)
        self.screen.fill(color_white)
        field = Field(self.screen, self.screen_height, self.screen_width, self.N)
        field.draw_field()
        field.draw_level()
        self.set_allies()
        self.set_enemies()

    def pause_game(self):
        """ The function is responsible for pause during the game """

    def end_game(self):
        """ The function is responsible for the end of the game """

    def reset_game(self):
        """ This function restarts the game """

    def next_turn(self):
        """

        :return:
        """

    def next_round(self):
        """

        :return:
        """

    def set_allies(self):
        """

        :return:
        """
        units_1 = []
        for i in range(rint(0, 3)):
            units_1.append(MeleeUnit(15, 6, 5, rint(1, self.N - 1) * (self.screen_height // (self.N + 1)),
                                     rint(self.N - self.N // 8, self.N - 1) * (self.screen_height // (self.N + 1)), 1, self.screen,
                                     self.cell_size))
            self.melee_number += 1
        for i in range(rint(0, 3)):
            units_1.append(RangeUnit(11, 4, 4, rint(1, self.N - 1) * (self.screen_height // (self.N + 1)),
                                     rint(self.N - self.N // 8, self.N - 1) * (self.screen_height // (self.N + 1)), 1, self.screen,
                                     self.cell_size))
            self.ranged_number += 1
        self.units_1 = units_1
        for i in units_1:
            i.draw_unit()

    def set_enemies(self):
        """

        :return:
        """
        units_2 = []
        for i in range(self.melee_number):
            units_2.append(MeleeUnit(15, 6, 5, rint(1, self.N - 1) * (self.screen_height // (self.N + 1)),
                                     rint(1, self.N // 8) * (self.screen_height // (self.N + 1)), 2, self.screen,
                                     self.cell_size))
        for i in range(self.ranged_number):
            units_2.append(RangeUnit(11, 4, 4, rint(1, self.N - 1) * (self.screen_height // (self.N + 1)),
                                     rint(1, self.N // 8) * (self.screen_height // (self.N + 1)), 2, self.screen,
                                     self.cell_size))
        self.units_2 = units_2
        for i in units_2:
            i.draw_unit()