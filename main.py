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
condition = 0  # 0 - Menu, 1 - game, 2 - endgame

pygame.init()
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("War tactics: call of DGAP")
clock = pygame.time.Clock()
menu_font = pygame.font.Font(None, 70)
game_font = pygame.font.Font(None, 30)
options = [Core.MainMenu("START GAME", (screen_height // 3 + 10, screen_width // 3 - 100), screen, menu_font),
           Core.MainMenu("EXIT", (2 * screen_height // 5 + 30, 2 * screen_width // 3 - 60), screen, menu_font)]
signs = [Bar("End turn", (cell_size * 2 * N // 3, cell_size * N + 5), screen, game_font),
         Bar("Exit Game", (cell_size * N * 5 // 6 + 20, cell_size * N + 5), screen, game_font),
         Bar("1", (cell_size * N // 10, cell_size * N + 5), screen, game_font),
         Bar("2", (cell_size * N // 10 + cell_size * 2, cell_size * N + 5), screen, game_font),
         Bar("3", (cell_size * N // 10 + cell_size * 4, cell_size * N + 5), screen, game_font),
         Bar("4", (cell_size * N // 10 + cell_size * 6, cell_size * N + 5), screen, game_font)]
victory1 = Bar("Player 1 WON!", (cell_size * N // 3, cell_size * N // 2), screen, menu_font)
victory2 = Bar("Player 2 WON!", (cell_size * N // 3, cell_size * N // 2), screen, menu_font)
game = Core.Game(screen, screen_height, screen_width, N, signs, game_font)
menu = pygame.image.load("pics/qop_arcana_bg.png").convert()
menu = pygame.transform.scale(menu, (screen_height, screen_height))
side = 0

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
                    game = Core.Game(screen, screen_height, screen_width, N, signs, game_font)
                    game.start_game()
                    condition = 1
                elif text == "EXIT":
                    finished = True
                    pygame.quit()
                    sys.exit()
            elif condition == 1:
                condition, side = game.check_end_game()
                game.redraw()
                game.draw_moves()
                game.unit.light()
                finish = Interface.game_event(event, game)
                if finish == 1:
                    condition = 0
                    signs = [Bar("End turn", (cell_size * 2 * N // 3, cell_size * N + 5), screen,
                                 game_font),
                             Bar("Exit Game", (cell_size * N * 5 // 6 + 20, cell_size * N + 5), screen,
                                 game_font),
                             Bar("1", (cell_size * N // 10, cell_size * N + 5), screen,
                                 game_font), Bar("2", (cell_size * N // 10 + cell_size * 2, cell_size * N + 5), screen,
                                                 game_font),
                             Bar("3", (cell_size * N // 10 + cell_size * 4, cell_size * N + 5), screen,
                                 game_font), Bar("4", (cell_size * N // 10 + cell_size * 6, cell_size * N + 5), screen,
                                                 game_font)]
                if game.unit.action_points == 0:
                    if game.unit == game.unit_order[len(game.unit_order) - 1]:
                        game.next_round()
                    else:
                        game.next_turn()
            elif condition == 2:
                screen.fill((255, 255, 255))
                if side == 1:
                    victory1.draw()
                else:
                    victory2.draw()

    pygame.display.update()
