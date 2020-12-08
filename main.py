import pygame
import sys
import Core
import Interface

finished = False
pygame.init()
screen_height = 840
screen_width = screen_height
N = 19
screen = pygame.display.set_mode((screen_height, screen_width))
clock = pygame.time.Clock()
menu_font = pygame.font.Font(None, 60)
options = [Core.MainMenu("START GAME", (screen_height // 3 + 30, screen_width // 3), screen, menu_font),
           Core.MainMenu("EXIT", (2 * screen_height // 5 + 40, 2 * screen_width // 3), screen,
                         menu_font)]
FPS = 20
condition = 0  # 0 - Menu, 1 - game

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            if condition == 0:
                text = Interface.menu_event(options)
                if text == "START GAME":
                    game = Core.Game(screen, screen_height, screen_width, N)
                    game.start_game()
                    condition = 1
                elif text == "EXIT":
                    finished = True
                    pygame.quit()
                    sys.exit()
            else:
                Interface.game_event(event)

    pygame.display.update()
