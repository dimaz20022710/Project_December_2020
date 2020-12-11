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
                    unit.special_ability()
                    game.update_info()

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
                                        unit.hit_status -= 1
                                        if aim.current_hp <= 0:
                                            aim.erase_pic()
                                            game.cells[aim.x // cell_size][aim.y // cell_size - 1][2] = 0
                                            del game.unit_order[game.unit_order.index(aim)]
                                else:
                                    unit.hit(aim)
                                    unit.hit_status -= 1
                                    if aim.current_hp <= 0:
                                        aim.erase_pic()
                                        game.cells[aim.x // cell_size][aim.y // cell_size - 1][2] = 0
                                        del game.unit_order[game.unit_order.index(aim)]
                                game.update_info()
    return 0
