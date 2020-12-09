from pygame.draw import rect
from abc import ABC, abstractmethod
from pygame import image


# range1 = image.load('pics/toy_sniper.png')


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
        pass

    def move_unit(self):
        """
        This function describes the movement of the unit
        """
        pass


class MeleeUnit(Unit):
    """
    A subclass of units that use melee combat
    """

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

    def draw_unit(self):
        if self.side == 1:
            rect(self.screen, (0, 255, 0), (self.x, self.y, self.cell_size, self.cell_size))
            rect(self.screen, (0, 0, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)
        else:
            rect(self.screen, (255, 0, 0), (self.x, self.y, self.cell_size, self.cell_size))
            rect(self.screen, (0, 0, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)

    def hit(self):
        """
        This function describes unit attacks
        """
        pass

    def special_ability(self):
        """
        This function describes the superpowers of individual units.
        """
        pass


class RangeUnit(Unit):
    """
    A subclass of units that use range combat
    """

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

    def draw_unit(self):
        if self.side == 1:
            rect(self.screen, (0, 0, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)
            rect(self.screen, (0, 105, 0), (self.x, self.y, self.cell_size, self.cell_size))
            # self.screen.blit(range1, (self.x, self.y))
        else:
            rect(self.screen, (0, 0, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)
            rect(self.screen, (105, 0, 0), (self.x, self.y, self.cell_size, self.cell_size))

    def hit(self):
        """
        This function describes unit attacks
        """
        pass

    def special_ability(self):
        """
        This function describes the superpowers of individual units.
        """
        pass
