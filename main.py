import pygame
import sys
import Core
import Interface
from Objects import Bar

finished = False
screen_height = 840
screen_width = screen_height
N = 19
cell_size = screen_height // (N + 1)
FPS = 20
condition = 0  # 0 - Menu, 1 - game

pygame.init()
screen = pygame.display.set_mode((screen_height, screen_width))
clock = pygame.time.Clock()
menu_font = pygame.font.Font(None, 60)
f1 = pygame.font.Font(None, 30)
options = [Core.MainMenu("START GAME", (screen_height // 3 + 30, screen_width // 3), screen, menu_font),
           Core.MainMenu("EXIT", (2 * screen_height // 5 + 40, 2 * screen_width // 3), screen,
                         menu_font)]
signs = [Bar("End turn", (cell_size * N // 3, cell_size * N + 15), screen,
             pygame.font.Font(None, 30)),
         Bar("Exit Game", (cell_size * N * 2 // 3, cell_size * N + 15), screen,
             pygame.font.Font(None, 30)), Bar("Special ability", (cell_size * 3 * N // 4, 5), screen,
                                              pygame.font.Font(None, 30))]
game = Core.Game(screen, screen_height, screen_width, N, signs, f1)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            if condition == 0:
                screen.fill((0, 0, 0))
                for option in options:
                    option.draw()
                text = Interface.menu_event(options)
                if text == "START GAME":
                    game = Core.Game(screen, screen_height, screen_width, N, signs, f1)
                    game.start_game()
                    condition = 1
                elif text == "EXIT":
                    finished = True
                    pygame.quit()
                    sys.exit()
            else:
                game.redraw()
                game.draw_moves()
                finish = Interface.game_event(event, signs, cell_size, game.cells, game.unit, game.unit_order, game)
                if finish == 1:
                    condition = 0
                    signs = [Bar("End turn", (cell_size * N // 3, cell_size * N + 15), screen,
                                 pygame.font.Font(None, 30)),
                             Bar("Exit Game", (cell_size * N * 2 // 3, cell_size * N + 15), screen,
                                 pygame.font.Font(None, 30)),
                             Bar("Special ability", (cell_size * 3 * N // 4, 5), screen,
                                 pygame.font.Font(None, 30))]
                if game.unit.current_movement <= 0 and game.unit.hit_status == 0:
                    if game.unit == game.unit_order[len(game.unit_order) - 1]:
                        game.next_round()
                    else:
                        game.next_turn()

    pygame.display.update()
