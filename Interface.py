import pygame
import sys
from pygame.locals import *

from Objects import MainMenu, Game


def start():
    pygame.init()
    clock = pygame.time.Clock()
    finished = False
    screen_height = 600
    screen_width = 600
    N = 19
    FPS = 30
    screen = pygame.display.set_mode((screen_height, screen_width))
    menu_font = pygame.font.Font(None, 40)
    options = [MainMenu("START GAME", (screen_height // 3, screen_width // 3), screen, menu_font),
               MainMenu("EXIT", (2 * screen_height // 5 + 20, 2 * screen_width // 3), screen, menu_font)]
    stop = 0
    while not finished:
        if stop == 0:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.event.pump()
            screen.fill((0, 0, 0))
            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        option.clicked = True
                        if option.text == "START GAME":
                            game = Game(pygame.display.set_mode((screen_height, screen_width)), screen_height,
                                        screen_width, N)
                            game.start_game()
                        else:
                            pygame.quit()
                            sys.exit()
                        stop = 1
                        break
                    else:
                        option.clicked = False
                else:
                    option.hovered = False
                    option.clicked = False
                option.draw()
                option.new_window()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        pygame.display.update()


start()
