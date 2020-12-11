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
        self.side = side
        self.screen = screen
        self.cell_size = cell_size
        self.current_movement = movement
        self.current_hp = hp
        self.hit_status = 1
        self.cooldown = 0
        self.current_damage = self.damage

    @abstractmethod
    def draw_unit(self):
        """
        This function draws a unit
        """
        pass

    def light(self):
        rect(self.screen, (255, 255, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)

    def unlight(self):
        rect(self.screen, (255, 255, 255), (self.x, self.y, self.cell_size, self.cell_size), 2)
        rect(self.screen, (0, 0, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)

    def erase_pic(self):
        rect(self.screen, (255, 255, 255), (self.x, self.y, self.cell_size, self.cell_size))
        rect(self.screen, (0, 0, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)

    def hit_bar(self):
        if self.side == 1:
            rect(self.screen, (0, 100, 0), (self.x, self.y - 20, self.cell_size, 10))
            rect(self.screen, (0, 200, 0), (self.x, self.y - 20, self.cell_size * self.current_hp // self.hp, 10))
        else:
            rect(self.screen, (100, 0, 0), (self.x, self.y - 20, self.cell_size, 10))
            rect(self.screen, (200, 0, 0), (self.x, self.y - 20, self.cell_size * self.current_hp // self.hp, 10))
        rect(self.screen, (0, 0, 0), (self.x, self.y - 20, self.cell_size, 10), 1)

    def move_unit(self, x, y):
        """
        This function describes the movement of the unit
        """
        self.erase_pic()
        self.unlight()
        self.x = x
        self.y = y
        self.draw_unit()
        self.light()


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
        self.type = "Melee"

    def draw_unit(self):
        if self.side == 1:
            rect(self.screen, (0, 255, 0), (self.x, self.y, self.cell_size, self.cell_size))
            rect(self.screen, (0, 0, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)
        else:
            rect(self.screen, (255, 0, 0), (self.x, self.y, self.cell_size, self.cell_size))
            rect(self.screen, (0, 0, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)
        self.hit_bar()

    def hit(self, aim):
        """
        This function describes unit attacks
        """
        aim.current_hp -= self.damage

    def special_ability(self):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown == 0:
            self.current_movement += self.movement
            self.cooldown = 3


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
        self.type = 'Range'

    def draw_unit(self):
        if self.side == 1:
            rect(self.screen, (0, 0, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)
            rect(self.screen, (0, 105, 0), (self.x, self.y, self.cell_size, self.cell_size))
            # self.screen.blit(range1, (self.x, self.y))
        else:
            rect(self.screen, (0, 0, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)
            rect(self.screen, (105, 0, 0), (self.x, self.y, self.cell_size, self.cell_size))
        self.hit_bar()

    def hit(self, aim):
        """
        This function describes unit attacks
        """
        aim.current_hp -= self.current_damage

    def special_ability(self):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown == 0:
            self.current_damage += self.damage
            self.cooldown = 3
