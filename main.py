import pygame
import sys
import Core
import Interface
from Objects import Bar

finished = False
pygame.init()
screen_height = 840
screen_width = screen_height
N = 19
cell_size = screen_height // (N + 1)
screen = pygame.display.set_mode((screen_height, screen_width))
clock = pygame.time.Clock()
menu_font = pygame.font.Font(None, 60)
options = [Core.MainMenu("START GAME", (screen_height // 3 + 30, screen_width // 3), screen, menu_font),
           Core.MainMenu("EXIT", (2 * screen_height // 5 + 40, 2 * screen_width // 3), screen,
                         menu_font)]
signs = [Bar("End turn", (cell_size * N // 3, cell_size * N + 15), screen,
             pygame.font.Font(None, 30)),
         Bar("Exit Game", (cell_size * N * 2 // 3, cell_size * N + 15), screen,
             pygame.font.Font(None, 30))]
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
                    game = Core.Game(screen, screen_height, screen_width, N, signs)
                    order, cells = game.start_game()
                    turn = 1
                    unit = order[turn - 1]
                    unit.light()
                    condition = 1
                elif text == "EXIT":
                    finished = True
                    pygame.quit()
                    sys.exit()
            else:
                Interface.game_event(event, signs, cell_size, cells, unit, order)
                if unit.current_movement <= 0 and unit.hit_status == 0:
                    if unit == order[len(order) - 1]:
                        unit.unlight()
                        turn = 1
                        unit = order[turn - 1]
                        unit.light()
                        for u in order:
                            u.hit_status = 1
                            u.current_movement = u.movement
                    else:
                        unit.unlight()
                        turn += 1
                        unit = order[turn - 1]
                        unit.light()

    pygame.display.update()
