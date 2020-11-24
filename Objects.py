import pygame, sys
from pygame.locals import *
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
        :param screen:
        :param x:
        :param y:
        :param height:
        :param width:
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw_wall(self):
        rect(self.screen, (0, 0, 0), (self.x, self.y), ())


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
    def __init__(self, screen, screen_height, screen_width, N):
        """

        """
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.N = N

    def start_game(self):
        """

        :return:
        """
        self.screen.fill((255, 255, 255))
        self.create_new_level()
        self.draw_level()

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

    def draw_field(self):
        """

        :return:
        """
        x1 = 0
        y1 = 0
        x2 = self.screen_width
        y2 = self.screen_height
        color = (0, 0, 0)
        rect(self.screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
        h = (x2 - x1) // (self.N + 1)
        x = x1 + h
        w = (y2 - y1) // (self.N + 1)
        y = y1 + w
        for i in range(self.N):
            line(self.screen, color, (x, y1), (x, y2))
            x += h
            line(self.screen, color, (x1, y), (x2, y))
            y += w

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
