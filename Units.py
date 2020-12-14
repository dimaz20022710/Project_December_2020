from pygame.draw import rect
from abc import ABC, abstractmethod
import math
import pygame


class Unit(ABC):
    """ This class describes units """

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """ This function will set the initial characteristics of an object of this class """
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
        self.ignore_walls = 0

    @abstractmethod
    def draw_unit(self):
        pass

    def light(self):
        """ The function draws yellow squares """
        color_yellow = (255, 255, 0)
        rect(self.screen, color_yellow, (self.x, self.y, self.cell_size, self.cell_size), 2)

    def unlight(self):
        """  This function turns off the light  """
        rect(self.screen, (255, 255, 255), (self.x, self.y, self.cell_size, self.cell_size), 2)
        rect(self.screen, (0, 0, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)

    def erase_pic(self):
        """ This function erases the unit """
        rect(self.screen, (255, 255, 255), (self.x, self.y, self.cell_size, self.cell_size))
        rect(self.screen, (0, 0, 0), (self.x, self.y, self.cell_size, self.cell_size), 2)

    def hit_bar(self):
        """ This function draws the health status of a unit """
        if self.side == 1:
            rect(self.screen, (0, 100, 0), (self.x, self.y - 20, self.cell_size, 10))
            rect(self.screen, (0, 200, 0), (self.x, self.y - 20, self.cell_size * self.current_hp // self.hp, 10))
        else:
            rect(self.screen, (100, 0, 0), (self.x, self.y - 20, self.cell_size, 10))
            rect(self.screen, (200, 0, 0), (self.x, self.y - 20, self.cell_size * self.current_hp // self.hp, 10))
        rect(self.screen, (0, 0, 0), (self.x, self.y - 20, self.cell_size, 10), 1)

    def move_unit(self, x, y):
        """ This function describes the movement of the unit """
        self.cells[self.x // self.cell_size][self.y // self.cell_size - 1][2] = 0
        self.erase_pic()
        self.unlight()
        self.x = x
        self.y = y
        self.cells[self.x // self.cell_size][self.y // self.cell_size - 1][2] = 1
        self.draw_unit()
        self.light()

    def check_walls(self, aim):
        """ This function checks for walls in the direction of the ability """
        k = 100
        points = []
        dy = (aim.y - self.y) / k
        dx = (aim.x - self.x) / k
        for i in range(k):
            points.append([self.x + math.ceil(i * dx), self.y + math.ceil(i * dy)])
        for i in self.cells:
            for j in i:
                for k in points:
                    if (k[0] - j[0] > 0) and (k[0] - j[0] < self.cell_size) and (k[1] - j[1] > 0) and (
                            k[1] - j[1] < self.cell_size):
                        if j[2] == -1:
                            return 1
        return 0

    @abstractmethod
    def special_ability1(self, cell):
        pass

    @abstractmethod
    def special_ability2(self, cell):
        pass

    @abstractmethod
    def special_ability3(self, cell):
        pass

    @abstractmethod
    def special_ability4(self, cell):
        pass


class MeleeUnit(Unit, ABC):
    """ A subclass of units that use melee combat """

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """ This function will set the initial characteristics of an object of this class """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
        self.type = "Melee"

    def hit(self, aim):
        """ This function describes unit attacks """
        if abs(self.x - aim.x) // self.cell_size < 2 and abs(self.y - aim.y) // self.cell_size < 2:
            aim.current_hp -= self.current_damage
            self.hit_status -= 1
            self.current_hp -= aim.back_dmg


class RangeUnit(Unit, ABC):
    """ A subclass of units that use range combat """

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """ This function will set the initial characteristics of an object of this class """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
        self.type = 'Range'

    def hit(self, aim):
        """ This function describes unit attacks """
        if self.ignore_walls == 0:
            if self.check_walls(aim) == 0:
                aim.current_hp -= self.current_damage
                self.hit_status -= 1
                self.current_hp -= aim.back_dmg
            else:
                self.hit_status -= 1
        else:
            aim.current_hp -= self.current_damage
            self.hit_status -= 1
            self.current_hp -= aim.back_dmg
            self.ignore_walls = 0


class Tank(MeleeUnit):

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """ This function will set the initial characteristics of an object of this class """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
        self.subclass = 'Tank'

        # Our tank
        self.wk = pygame.image.load("pics/wk.jfif").convert()
        self.wk = pygame.transform.scale(self.wk, (self.cell_size, self.cell_size))
        # Opponent's tank
        self.axe = pygame.image.load("pics/axe.png").convert()
        self.axe = pygame.transform.scale(self.axe, (self.cell_size, self.cell_size))

    def draw_unit(self):
        """ This function draws tanks on the field """
        if self.side == 1:
            self.screen.blit(self.wk, (self.x, self.y))
        else:
            self.screen.blit(self.axe, (self.x, self.y))
        self.hit_bar()

    def special_ability1(self, cell):
        """ Blaidmail - This ability allows the tank to return damage taken to the enemy """
        if self.cooldown1 == 0:
            self.back_dmg = 15
            self.cooldown1 = 3
        self.clicked = False

    def special_ability2(self, cell):
        """ Speed up! - This ability increases the radius of the cells for the tank."""
        if self.cooldown2 == 0:
            self.current_movement += self.movement
            self.cooldown2 = 3
        self.clicked = False

    def special_ability3(self, cell):
        """ <Passive> heal - This ability allows the tank to replenish its health."""
        if self.cooldown3 == 0:
            self.current_hp += 5
            self.cooldown3 = 1
        self.clicked = False

    def special_ability4(self, unit):
        """ Duel - This ability allows you to aggro the enemy for 2 turns """
        if self.cooldown4 == 0:
            if type(unit) != list:
                if self.check_walls(unit) == 0:
                    unit.agred = 2
                self.cooldown4 = 5
                self.clicked = False
        else:
            self.clicked = False


class Rogue(MeleeUnit):

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """ This function will set the initial characteristics of an object of this class """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
        self.subclass = 'Rogue'

        # Our rogue
        self.Furion = pygame.image.load("pics/furion.jpg").convert()
        self.Furion = pygame.transform.scale(self.Furion, (self.cell_size, self.cell_size))
        # Opponent's rogue
        self.lega = pygame.image.load("pics/Lega.jfif").convert()
        self.lega = pygame.transform.scale(self.lega, (self.cell_size, self.cell_size))

    def draw_unit(self):
        """ This function draws rogues on the field """
        if self.side == 1:
            self.screen.blit(self.Furion, (self.x, self.y))
        else:
            self.screen.blit(self.lega, (self.x, self.y))
        self.hit_bar()

    def special_ability1(self, unit):
        """ This function describes the superpowers of individual units """
        if self.cooldown1 == 0:
            if type(unit) != list:
                if self.check_walls(unit) == 0:
                    unit.current_movement = 0
                self.cooldown1 = 3
                self.clicked = False
        else:
            self.clicked = False

    def special_ability2(self, cell):
        """ This ability allows one extra hit """
        if self.cooldown2 == 0:
            self.hit_status += 1
            self.cooldown2 = 3
            self.clicked = False
        else:
            self.clicked = False

    def special_ability3(self, cell):
        """ This ability allows you to deal critical damage """
        if self.cooldown3 == 0:
            self.current_damage += self.damage * 2 // 3
            self.cooldown3 = 2
            self.clicked = False
        else:
            self.clicked = False

    def special_ability4(self, cell):
        """ This ability allows you to teleport to any cell on the field """
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
        """ This function will set the initial characteristics of an object of this class """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
        self.subclass = 'Wizard'
        # Our wizard
        self.pugna = pygame.image.load("pics/pugna.png").convert()
        self.pugna = pygame.transform.scale(self.pugna, (self.cell_size, self.cell_size))
        # Opponent's wizard
        self.invoker = pygame.image.load("pics/Invo.jfif").convert()
        self.invoker = pygame.transform.scale(self.invoker, (self.cell_size, self.cell_size))

    def draw_unit(self):
        """ This function draws wizards on the field """
        if self.side == 1:
            self.screen.blit(self.pugna, (self.x, self.y))
        else:
            self.screen.blit(self.invoker, (self.x, self.y))
        self.hit_bar()

    def special_ability1(self, unit):
        """ This ability allows you to freeze the enemy for 2 turns """
        if self.cooldown1 == 0:
            if type(unit) != list:
                if self.check_walls(unit) == 0:
                    unit.stunned = 2
                self.cooldown1 = 4
                self.clicked = False
        else:
            self.clicked = False

    def special_ability2(self, unit):
        """ This ability allows you to deal 30 damage """
        if self.cooldown2 == 0:
            if type(unit) != list:
                if self.check_walls(unit) == 0:
                    unit.current_hp -= 30
                self.cooldown2 = 4
                self.clicked = False
        else:
            self.clicked = False

    def special_ability3(self, unit):
        """ This ability allows you to deal 10 damage and halve the enemy's movement radius """
        if self.cooldown3 == 0:
            if type(unit) != list:
                if self.check_walls(unit) == 0:
                    unit.current_hp -= 10
                    unit.current_movement //= 2
                self.cooldown3 = 2
                self.clicked = False
        else:
            self.clicked = False

    def special_ability4(self, unit):
        """ This ability allows you to increase the cooldown of enemy abilities """
        if self.cooldown4 == 0:
            if type(unit) != list:
                if self.check_walls(unit) == 0:
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
        """ This function will set the initial characteristics of an object of this class """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
        self.subclass = 'Sniper'
        # Our sniper
        self.sniper = pygame.image.load("pics/Sniper.png")
        self.sniper = pygame.transform.scale(self.sniper, (self.cell_size, self.cell_size))
        # Opponent's sniper
        self.Gyro = pygame.image.load("pics/Gyro.jfif")
        self.Gyro = pygame.transform.scale(self.Gyro, (self.cell_size, self.cell_size))

    def draw_unit(self):
        """ This function draws snipers on the field """
        if self.side == 1:
            self.screen.blit(self.sniper, (self.x, self.y))
        else:
            self.screen.blit(self.Gyro, (self.x, self.y))
        self.hit_bar()

    def special_ability1(self, cell):
        """ This ability increases the sniper's damage by 1.5 times """
        if self.cooldown1 == 0:
            self.current_damage += self.damage // 2
            self.cooldown1 = 1
            self.clicked = False
        else:
            self.clicked = False

    def special_ability2(self, cell):
        """ This ability increases the sniper's movement radius """
        if self.cooldown2 == 0:
            self.ignore_walls = 1
            self.cooldown2 = 2
        self.clicked = False

    def special_ability3(self, unit):
        """ This ability allows you to deal 20 additional damage """
        if self.cooldown3 == 0:
            if type(unit) != list:
                if self.check_walls(unit) == 0:
                    unit.current_hp -= 20
                self.cooldown3 = 4
                self.clicked = False
        else:
            self.clicked = False

    def special_ability4(self, unit):
        """ This ability allows you to reduce the radius of movement of the enemy by 3 times """
        if self.cooldown4 == 0:
            if type(unit) != list:
                if self.check_walls(unit) == 0:
                    unit.movement -= unit.movement // 3
                self.cooldown4 = 4
                self.clicked = False
        else:
            self.clicked = False


class Support(RangeUnit):

    def __init__(self, hp, damage, movement, x, y, side, screen, cell_size, cells):
        """ This function will set the initial characteristics of an object of this class """
        super().__init__(hp, damage, movement, x, y, side, screen, cell_size, cells)
        self.subclass = 'Support'
        # Our support
        self.Crystal_maiden = pygame.image.load("pics/crystal_maiden_vert.jpg").convert()
        self.Crystal_maiden = pygame.transform.scale(self.Crystal_maiden, (self.cell_size, self.cell_size))
        # Enemy support
        self.Lion = pygame.image.load("pics/Lion.jfif").convert()
        self.Lion = pygame.transform.scale(self.Lion, (self.cell_size, self.cell_size))

    def draw_unit(self):
        """ This function draws supports on the field """
        if self.side == 1:
            self.screen.blit(self.Crystal_maiden, (self.x, self.y))
        else:
            self.screen.blit(self.Lion, (self.x, self.y))
        self.hit_bar()

    def special_ability1(self, unit):
        """ This ability restores 20 health to an ally """
        if self.cooldown1 == 0:
            if type(unit) != list:
                if self.check_walls(unit) == 0:
                    unit.current_hp += 20
                    if unit.current_hp > unit.hp:
                        unit.current_hp = unit.hp
                self.cooldown1 = 2
                self.clicked = False
        else:
            self.clicked = False

    def special_ability2(self, unit):
        """ This ability allows an ally to be invulnerable for spells for 2 turns """
        if self.cooldown2 == 0:
            if type(unit) != list:
                if self.check_walls(unit) == 0:
                    unit.protection = 2
                self.cooldown2 = 2
                self.clicked = False
        else:
            self.clicked = False

    def special_ability3(self, unit):
        """ This ability allows you to deal 1 damage and immobilize the enemy for 2 turns """
        if self.cooldown3 == 0:
            if type(unit) != list:
                if self.check_walls(unit) == 0:
                    unit.current_hp -= 10
                    unit.stunned = 2
                self.cooldown3 = 4
                self.clicked = False
        else:
            self.clicked = False

    def special_ability4(self, unit):
        """ This ability restores 50 health to an ally """
        if self.cooldown4 == 0:
            if type(unit) != list:
                unit.current_hp += 50
                if unit.current_hp > unit.hp:
                    unit.current_hp = unit.hp
                self.cooldown4 = 4
                self.clicked = False
        else:
            self.clicked = False
