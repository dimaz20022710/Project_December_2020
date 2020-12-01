import pygame
import sys
from pygame.locals import *

#from Objects import MainMenu, Game


class Window:

    def __init__(self, screen_height, screen_width, N, FPS):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen = pygame.display.set_mode((self.screen_height, self.screen_width))
        self.N = N
        self.FPS = FPS

    def start(self):
        pygame.init()
        clock = pygame.time.Clock()
        finished = False
        menu_font = pygame.font.Font(None, 40)
        options = [MainMenu("START GAME", (self.screen_height // 3, self.screen_width // 3), self.screen, menu_font),
                   MainMenu("EXIT", (2 * self.screen_height // 5 + 20, 2 * self.screen_width // 3), self.screen,
                            menu_font)]
        stop = 0
        while not finished:
            if stop == 0:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.event.pump()
                self.screen.fill((0, 0, 0))
                for option in options:
                    if option.rect.collidepoint(pygame.mouse.get_pos()):
                        option.hovered = True
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            option.clicked = True
                            if option.text == "START GAME":
                                '''game = Game(pygame.display.set_mode((screen_height, screen_width)), screen_height,
                                            screen_width, N)'''
                                Game.start_game()
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
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
            pygame.display.update()

# start()
