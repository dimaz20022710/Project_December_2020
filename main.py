import pygame
import sys
import Core
import Interface
from Objects import Bar

finished = False
screen_height = 840
screen_width = screen_height
N = 23
cell_size = screen_height // (N + 1)
FPS = 30
condition = 0  # 0 - Menu, 1 - game

pygame.init()
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("WarGame")
clock = pygame.time.Clock()
menu_font = pygame.font.Font(None, 60)
f1 = pygame.font.Font(None, 30)
options = [Core.MainMenu("START GAME", (screen_height // 3 + 10, screen_width // 3 - 100), screen, menu_font),
           Core.MainMenu("EXIT", (2 * screen_height // 5 + 40, 2 * screen_width // 3 - 150), screen,
                         menu_font)]
signs = [Bar("End turn", (cell_size * 2 * N // 3, cell_size * N + 5), screen,
             pygame.font.Font(None, 30)),
         Bar("Exit Game", (cell_size * N * 5 // 6 + 20, cell_size * N + 5), screen,
             pygame.font.Font(None, 30)),
         Bar("1", (cell_size * N // 10, cell_size * N + 5), screen,
             f1), Bar("2", (cell_size * N // 10 + cell_size * 2, cell_size * N + 5), screen,
                      f1), Bar("3", (cell_size * N // 10 + cell_size * 4, cell_size * N + 5), screen,
                               f1), Bar("4", (cell_size * N // 10 + cell_size * 6, cell_size * N + 5), screen,
                                        f1)]
game = Core.Game(screen, screen_height, screen_width, N, signs, f1)
menu = pygame.image.load("pics/qop_arcana_bg.png").convert()
menu = pygame.transform.scale(menu, (screen_height, screen_height))


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            if condition == 0:
                screen.blit(menu, (0, 0))
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
                game.unit.light()
                finish = Interface.game_event(event, signs, cell_size, game.cells, game.unit, game.unit_order, game)
                if finish == 1:
                    condition = 0
                    signs = [Bar("End turn", (cell_size * N // 3, cell_size * N + 15), screen,
                                 pygame.font.Font(None, 30)),
                             Bar("Exit Game", (cell_size * N * 2 // 3, cell_size * N + 15), screen,
                                 pygame.font.Font(None, 30)),
                             Bar("Special ability", (cell_size * 3 * N // 4, 5), screen,
                                 pygame.font.Font(None, 30))]
                if game.unit.hit_status == 0:
                    if game.unit == game.unit_order[len(game.unit_order) - 1]:
                        game.next_round()
                    else:
                        game.next_turn()

    pygame.display.update()
