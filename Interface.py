import pygame, sys
from pygame.locals import *
from Objects import MainMenu, Game


def start():
    pygame.init()
    screen = pygame.display.set_mode((480, 320))
    menu_font = pygame.font.Font(None, 40)
    options = [MainMenu("START GAME", (140, 105), screen, menu_font), MainMenu("EXIT", (185, 205), screen, menu_font)]
    while True:
        stop = 0
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
                        game = Game(pygame.display.set_mode((480, 320)))
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
        pygame.display.update()
        if stop == 1:
            break


start()
