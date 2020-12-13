from pygame.draw import rect
from abc import ABC, abstractmethod
from pygame import image
from Objects import check_walls


# range1 = image.load('pics/toy_sniper.png')


class Unit(ABC):
    """
    This class describes units
    """

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
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
        self.cells = cells
        self.current_movement = movement
        self.current_hp = hp
        self.hit_status = 1
        self.current_damage = self.damage
        self.cooldown1 = 0
        self.cooldown2 = 0
        self.cooldown3 = 0
        self.cooldown4 = 0
        self.back_dmg = 0
        self.clicked = False
        self.agred = 0
        self.stunned = 0
        self.protection = 0
        self.ability = 0

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
        self.cells[self.x // self.cell_size][self.y // self.cell_size - 1][2] = 0
        self.erase_pic()
        self.unlight()
        self.x = x
        self.y = y
        self.cells[self.x // self.cell_size][self.y // self.cell_size - 1][2] = 1
        self.draw_unit()
        self.light()

    @abstractmethod
    def special_ability1(self, cell):
        """
        This function describes the superpowers of individual units.
        """
        pass

    @abstractmethod
    def special_ability2(self, cell):
        """
        This function describes the superpowers of individual units.
        """
        pass

    @abstractmethod
    def special_ability3(self, cell):
        """
        This function describes the superpowers of individual units.
        """
        pass

    @abstractmethod
    def special_ability4(self, cell):
        """
        This function describes the superpowers of individual units.
        """
        pass


class MeleeUnit(Unit, ABC):
    """
    A subclass of units that use melee combat
    """

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """
        This function will set the initial characteristics of an object of this class
        :param hp: Unit's health
        :param damage: Unit's damage
        :param movement: Unit's speed
        :param x: Unit's coordinate x
        :param y: Unit's coordinate y
        """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
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
        if abs(self.x - aim.x) // self.cell_size < 2 and abs(self.y - aim.y) // self.cell_size < 2:
            aim.current_hp -= self.current_damage
            self.hit_status -= 1
            self.current_hp -= aim.back_dmg


class RangeUnit(Unit, ABC):
    """
    A subclass of units that use range combat
    """

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """
        This function will set the initial characteristics of an object of this class
        :param hp: Unit's health
        :param damage: Unit's damage
        :param movement: Unit's speed
        :param x: Unit's coordinate x
        :param y: Unit's coordinate y
        """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
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
        if check_walls(self, aim, self.cell_size, self.cells) == 0:
            aim.current_hp -= self.current_damage
            self.hit_status -= 1
            self.current_hp -= aim.back_dmg
        else:
            self.hit_status -= 1


class Tank(MeleeUnit):

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """
        This function will set the initial characteristics of an object of this class
        :param hp: Unit's health
        :param damage: Unit's damage
        :param movement: Unit's speed
        :param x: Unit's coordinate x
        :param y: Unit's coordinate y
        """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
        self.subclass = 'Tank'

    def special_ability1(self, cell):
        """
        Blaidmail
        """
        if self.cooldown1 == 0:
            self.back_dmg = 15
            self.cooldown1 = 3
        self.clicked = False

    def special_ability2(self, cell):
        """
        Speed up!
        """
        if self.cooldown2 == 0:
            self.current_movement += self.movement
            self.cooldown2 = 3
        self.clicked = False

    def special_ability3(self, cell):
        """
        <Passive> heal
        """
        if self.cooldown3 == 0:
            self.current_hp += 5
            self.cooldown3 = 1
        self.clicked = False

    def special_ability4(self, unit):
        """
        Duel
        """
        if self.cooldown4 == 0:
            if type(unit) != list:
                unit.agred = 2
                self.cooldown4 = 5
                self.clicked = False
        else:
            self.clicked = False


class Rogue(MeleeUnit):

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """
        This function will set the initial characteristics of an object of this class
        :param hp: Unit's health
        :param damage: Unit's damage
        :param movement: Unit's speed
        :param x: Unit's coordinate x
        :param y: Unit's coordinate y
        """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
        self.subclass = 'Rogue'

    def special_ability1(self, unit):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown1 == 0:
            if type(unit) != list:
                unit.current_movement = 0
                self.cooldown1 = 3
                self.clicked = False
        else:
            self.clicked = False

    def special_ability2(self, cell):
        """
        Additional hit
        """
        if self.cooldown2 == 0:
            self.hit_status += 1
            self.cooldown2 = 3
            self.clicked = False
        else:
            self.clicked = False

    def special_ability3(self, cell):
        """
        Critical dmg
        """
        if self.cooldown3 == 0:
            self.current_damage += self.damage * 2 // 3
            self.cooldown3 = 2
            self.clicked = False
        else:
            self.clicked = False

    def special_ability4(self, cell):
        """
        Instant teleportation
        """
        if self.cooldown4 == 0:
            if type(cell) == list:
                if cell[2] == 0:
                    self.move_unit(cell[0], cell[1])
                    self.cooldown4 = 4
                    self.clicked = False
        else:
            self.clicked = False


class Wizard(RangeUnit):

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """
        This function will set the initial characteristics of an object of this class
        :param hp: Unit's health
        :param damage: Unit's damage
        :param movement: Unit's speed
        :param x: Unit's coordinate x
        :param y: Unit's coordinate y
        """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
        self.subclass = 'Wizard'

    def special_ability1(self, unit):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown1 == 0:
            if type(unit) != list:
                unit.stunned = 2
                self.cooldown1 = 4
                self.clicked = False
        else:
            self.clicked = False

    def special_ability2(self, unit):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown2 == 0:
            if type(unit) != list:
                unit.current_hp -= 30
                self.cooldown2 = 4
                self.clicked = False
        else:
            self.clicked = False

    def special_ability3(self, unit):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown3 == 0:
            if type(unit) != list:
                unit.current_hp -= 10
                unit.current_movement //= 2
                self.cooldown3 = 2
                self.clicked = False
        else:
            self.clicked = False

    def special_ability4(self, unit):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown4 == 0:
            if type(unit) != list:
                unit.cooldown1 += 1
                unit.cooldown2 += 1
                unit.cooldown3 += 1
                unit.cooldown4 += 1
                self.cooldown4 = 4
                self.clicked = False
        else:
            self.clicked = False


class Sniper(RangeUnit):

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """
        This function will set the initial characteristics of an object of this class
        :param hp: Unit's health
        :param damage: Unit's damage
        :param movement: Unit's speed
        :param x: Unit's coordinate x
        :param y: Unit's coordinate y
        """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
        self.subclass = 'Sniper'

    def special_ability1(self, cell):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown1 == 0:
            self.current_damage += self.damage // 2
            self.cooldown1 = 1
            self.clicked = False
        else:
            self.clicked = False

    def special_ability2(self, cell):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown2 == 0:
            self.current_movement += self.movement
            self.cooldown2 = 3
        self.clicked = False

    def special_ability3(self, unit):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown3 == 0:
            if type(unit) != list:
                unit.current_hp -= 20
                self.cooldown3 = 4
                self.clicked = False
        else:
            self.clicked = False

    def special_ability4(self, unit):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown4 == 0:
            if type(unit) != list:
                unit.movement -= unit.movement // 3
                self.cooldown4 = 4
                self.clicked = False
        else:
            self.clicked = False


class Support(MeleeUnit):

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """
        This function will set the initial characteristics of an object of this class
        :param hp: Unit's health
        :param damage: Unit's damage
        :param movement: Unit's speed
        :param x: Unit's coordinate x
        :param y: Unit's coordinate y
        """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
        self.subclass = 'Support'

    def special_ability1(self, unit):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown1 == 0:
            if type(unit) != list:
                unit.current_hp += 20
                if unit.current_hp > unit.hp:
                    unit.current_hp = unit.hp
                self.cooldown1 = 2
                self.clicked = False
        else:
            self.clicked = False

    def special_ability2(self, unit):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown2 == 0:
            if type(unit) != list:
                unit.protection = 2
                self.cooldown2 = 2
                self.clicked = False
        else:
            self.clicked = False

    def special_ability3(self, unit):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown3 == 0:
            if type(unit) != list:
                unit.current_hp -= 15
                unit.stunned = 2
                self.cooldown3 = 4
                self.clicked = False
        else:
            self.clicked = False

    def special_ability4(self, unit):
        """
        This function describes the superpowers of individual units.
        """
        if self.cooldown4 == 0:
            if type(unit) != list:
                unit.current_hp += 50
                if unit.current_hp > unit.hp:
                    unit.current_hp = unit.hp
                self.cooldown4 = 4
                self.clicked = False
        else:
            self.clicked = False
