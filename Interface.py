import pygame


def menu_event(options):
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
            if pygame.mouse.get_pressed() == (1, 0, 0):
                option.clicked = True
                return option.text
            else:
                option.clicked = False
        else:
            option.hovered = False
            option.clicked = False
        option.draw()
        option.new_window()


def game_event(event, signs, cell_size, cells):

    if event.type == pygame.MOUSEBUTTONDOWN:
        for sign in signs:
            if sign.rect.collidepoint(event.pos):
                sign.hovered = True
                if sign == signs[0]:
                    pass
                if sign == signs[1]:
                    pass
        for i in cells:
            for j in i:
                if j[2] == 0:
                    pass
                if j[2] == 1:
                    pass



