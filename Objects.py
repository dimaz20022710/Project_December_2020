class Unit:
    """
    Describes a unit
    """

    def __init__(self, hp, damage, movement, x, y):
        self.hp = hp
        self.damage = damage
        self.movement = movement
        self.x = x
        self.y = y

    def draw_unit(self):
        """

        :return:
        """

    def move_unit(self):
        """

        :return:
        """


class MeleeUnit(Unit):
    """

    """

    def __init__(self, hp, damage, movement, x, y):
        super().__init__(hp, damage, movement, x, y)

    def hit(self):
        """

        :return:
        """

    def special_ability(self):
        """

        :return:
        """


class RangeUnit(Unit):
    """

    """

    def __init__(self, hp, damage, movement, x, y):
        super().__init__(hp, damage, movement, x, y)

    def hit(self):
        """

        :return:
        """

    def special_ability(self):
        """

        :return:
        """


class Wall:
    """

    """

    x = 0

    y = 0


class MainMenu:
    hovered = False
    clicked = False

    def __init__(self, text, pos, screen, menu_font):
        self.text = text
        self.pos = pos
        self.screen = screen
        self.menu_font = menu_font
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        self.screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = self.menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            if self.clicked:
                return (255, 0, 0)
            else:
                return (255, 255, 255)
        else:
            return (100, 100, 100)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def new_window(self):
        if self.clicked:
            self.screen.fill((159, 182, 205))
        else:
            pass


class Game:
    def __init__(self):
        """

        """

    def start_game(self):
        """

        :return:
        """

    def pause_game(self):
        """

        :return:
        """

    def end_game(self):
        """

        :return:
        """

    def reset_game(self):
        """

        :return:
        """

    def create_new_level(self):
        """

       :return:
       """

    def next_turn(self):
        """

        :return:
        """

    def next_round(self):
        """

        :return:
        """

