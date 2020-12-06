import pygame
import sys
import Objects
import Core
import Interface

finished = False
pygame.init()
screen_height = 600
screen_width = screen_height
N = 19
screen = pygame.display.set_mode((screen_height, screen_width))
clock = pygame.time.Clock()
menu_font = pygame.font.Font(None, 40)
options = [Objects.MainMenu("START GAME", (screen_height // 3, screen_width // 3), screen, menu_font),
           Objects.MainMenu("EXIT", (2 * screen_height // 5 + 20, 2 * screen_width // 3), screen,
                            menu_font)]
FPS = 20
condition = 0


while not finished:
    #pygame.event.pump()
    #screen.fill((0, 0, 0))
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            if condition == 0:
                text = Interface.menu_event(options)
                if text == "START GAME":
                    game = Objects.Game(screen, screen_height, screen_width, N)
                    game.start_game()
                    condition = 1
                elif text == "EXIT":
                    finished = True
                    pygame.quit()
                    sys.exit()
            else:
                Interface.game_event(event)

    pygame.display.update()

'''game = Objects.Game(screen_height=600, screen_width=600, N=19, FPS=20)
game.start(game)'''
