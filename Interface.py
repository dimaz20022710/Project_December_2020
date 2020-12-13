import pygame


def menu_event(options):
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
            if pygame.mouse.get_pressed(3) == (1, 0, 0):
                option.clicked = True
                return option.text
            else:
                option.clicked = False
        else:
            option.hovered = False
            option.clicked = False
        option.draw()
        option.new_window()


def game_event(event, signs, cell_size, cells, unit, order, game):
    if event.type == pygame.MOUSEBUTTONDOWN:
        for sign in signs:
            if sign.rect.collidepoint(event.pos):
                sign.hovered = True
                if sign == signs[0]:
                    unit.current_movement = 0
                    unit.hit_status = 0
                    game.update_info()
                if sign == signs[1]:
                    return 1
                if sign == signs[2]:
                    unit.ability = 1
                    unit.clicked = True
                    unit.special_ability1(cells[unit.x // cell_size][unit.y // cell_size - 1])
                    game.update_info()
                if sign == signs[3]:
                    unit.ability = 2
                    unit.clicked = True
                    unit.special_ability2(cells[unit.x // cell_size][unit.y // cell_size - 1])
                    game.update_info()
                if sign == signs[4]:
                    unit.ability = 3
                    unit.clicked = True
                    unit.special_ability3(cells[unit.x // cell_size][unit.y // cell_size - 1])
                    game.update_info()
                if sign == signs[5]:
                    unit.ability = 4
                    unit.clicked = True
                    unit.special_ability4(cells[unit.x // cell_size][unit.y // cell_size - 1])
                    game.update_info()
        if not unit.clicked:
            for i in cells:
                for j in i:
                    if (event.pos[0] - j[0] > 0) and (event.pos[0] - j[0] < cell_size) and (event.pos[1] - j[1] > 0) and (
                            event.pos[1] - j[1] < cell_size):
                        if j[2] == 0:
                            if abs(j[0] - unit.x) // cell_size + abs(
                                    j[1] - unit.y) // cell_size <= unit.current_movement and unit.current_movement > 0:
                                unit.current_movement -= abs(j[0] - unit.x) // cell_size + abs(j[1] - unit.y) // cell_size
                                cells[unit.x // cell_size][unit.y // cell_size - 1][2] = 0
                                unit.move_unit(j[0], j[1])
                                j[2] = 1
                                game.update_info()
                        if j[2] == 1:
                            for aim in order:
                                if aim.x == j[0] and aim.y == j[1] and aim.side != unit.side and unit.hit_status != 0:
                                    if unit.type == 'Melee':
                                        if abs(unit.x - aim.x) // cell_size < 2 and abs(unit.y - aim.y) // cell_size < 2:
                                            unit.hit(aim)
                                            if aim.current_hp <= 0:
                                                game.unit_death(aim)
                                    else:
                                        unit.hit(aim)
                                        if aim.current_hp <= 0:
                                            game.unit_death(aim)
                                    game.update_info()
        else:
            for i in cells:
                for j in i:
                    if (event.pos[0] - j[0] > 0) and (event.pos[0] - j[0] < cell_size) and (event.pos[1] - j[1] > 0) and (
                            event.pos[1] - j[1] < cell_size):
                        game.use_ability(j)
                        game.update_info()
    return 0

