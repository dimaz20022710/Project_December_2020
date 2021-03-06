from Objects import Field
from random import randint as randint
from Units import Tank, Rogue, Support, Wizard, Sniper
from pygame.draw import rect


class MainMenu:
    """ This is the class responsible for the main menu """
    hovered = False
    clicked = False

    def __init__(self, text, pos, screen, menu_font):
        """ This function sets the initial conditions for an object from this class """
        self.text = text
        self.pos = pos
        self.screen = screen
        self.menu_font = menu_font
        self.set_rect()
        self.draw()

    def draw(self):
        """ This function draws a menu screen """
        self.set_rend()
        self.screen.blit(self.rend, self.rect)

    def set_rend(self):
        """ This function renders the menu """
        self.rend = self.menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        """ This function changes the color of the button in the menu """
        color_red = (255, 0, 0)
        color_white = (255, 255, 255)

        if self.hovered:
            if self.clicked:
                return color_red
            else:
                return color_red
        else:
            return color_white

    def set_rect(self):
        """ This function is responsible for the interaction of the player with the buttons in the menu. """
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def new_window(self):
        """ This function creates a new window """
        color_blue = (159, 182, 205)
        if self.clicked:
            self.screen.fill(color_blue)
        else:
            pass


class Game:
    """ This class is responsible for the game process """

    def __init__(self, screen, screen_height, screen_width, N, signs, f1):
        """ This function is responsible for the initial screen characteristics when creating an object of this class
        """

        self.unit_order = []
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.screen = screen
        self.N = N
        self.signs = signs
        self.font = f1
        self.cell_size = (self.screen_height // (self.N + 1))
        self.units_1 = []
        self.units_2 = []
        self.cells = []
        self.turn = 1

    def start_game(self):
        """ This function starts the game """
        color_white = (255, 255, 255)
        self.screen.fill(color_white)
        field = Field(self.screen, self.screen_height, self.screen_width, self.N)
        self.cells = field.draw_map()
        self.set_allies()
        self.set_enemies()
        for i in range(len(self.units_1)):
            self.unit_order.append(self.units_1[i])
            self.unit_order.append(self.units_2[i])
        self.unit = self.unit_order[0]
        self.unit.light()
        for sign in self.signs:
            sign.draw()
        self.update_info()

    def check_end_game(self):
        """ This function checks if the game is ended """
        fin = 0
        for unit in self.unit_order:
            if unit.side == 1:
                fin += 1
        if fin == len(self.unit_order):
            return 2, 1
        elif fin == 0:
            return 2, 2
        else:
            return 1, 0

    def lighten_cell(self, x, y):
        """ This function makes the cells available for turn yellow """
        color_black = (0, 0, 0)
        color_yellow = (230, 230, 0)
        rect(self.screen, color_yellow, (x, y, self.cell_size, self.cell_size))
        rect(self.screen, color_black, (x, y, self.cell_size, self.cell_size), 2)

    def unit_death(self, aim):
        """ This function handles the death of a character """
        aim.erase_pic()
        self.cells[aim.x // self.cell_size][aim.y // self.cell_size - 1][2] = 0
        if self.unit_order.index(aim) < self.unit_order.index(self.unit):
            self.turn -= 1
        del self.unit_order[self.unit_order.index(aim)]

    def redraw(self):
        """ This function checks the death of the unit and draws it depending on it """
        color_black = (0, 0, 0)
        color_white = (255, 255, 255)
        for c in self.cells:
            for cell in c:
                if cell[2] == -1:
                    rect(self.screen, color_black, (cell[0], cell[1], self.cell_size, self.cell_size))
                if cell[2] == 0:
                    rect(self.screen, color_white, (cell[0], cell[1], self.cell_size, self.cell_size))
                    rect(self.screen, color_black, (cell[0], cell[1], self.cell_size, self.cell_size), 2)
                if cell[2] == 1:
                    for unit in self.unit_order:
                        if cell[0] == unit.x and cell[1] == unit.y:
                            unit.draw_unit()

    def draw_moves(self):
        """ This function handles the movement of the hero """
        for i in range(-self.unit.current_movement, self.unit.current_movement + 1):
            for j in range(-self.unit.current_movement, self.unit.current_movement + 1):
                if self.unit.current_movement >= abs(i) + abs(j) > 0:
                    if (self.N + 1 > self.unit.x // self.cell_size + i >= 0) and (
                            self.N > self.unit.y // self.cell_size + j > 0):
                        if self.cells[self.unit.x // self.cell_size + i][self.unit.y // self.cell_size + j - 1][2] == 0:
                            self.lighten_cell(self.unit.x + i * self.cell_size, self.unit.y + j * self.cell_size)
        for unit in self.unit_order:
            unit.hit_bar()

    def update_info(self):
        """ This function processes information about the characters and displays the field depending on this. """
        color_white = (255, 255, 255)
        rect(self.screen, color_white, (0, 0, self.screen_height, self.cell_size))
        text = self.font.render(
            'Player ' + str(self.unit.side) + ' , ' + str(self.unit.subclass) + ', hp - ' + str(
                self.unit.current_hp) + ', movement - ' + str(
                self.unit.current_movement) + ', ap - ' + str(
                self.unit.action_points) + ', cd1 - ' + str(self.unit.cooldown1) + ', cd2 - ' + str(self.unit.cooldown2)
            + ', cd3 - ' + str(self.unit.cooldown3) + ', cd4 - ' + str(self.unit.cooldown4), False,
            (0, 0, 0))
        self.screen.blit(text, (15, 0))

    def next_turn(self):
        """ This function allows you to transfer the move to another player """
        self.unit.unlight()
        self.turn += 1
        self.unit = self.unit_order[self.turn - 1]
        self.unit.light()
        if self.unit.protection <= 0:
            if self.unit.agred > 0:
                if self.unit.side == 1:
                    self.unit.hit(self.units_2[0])
                else:
                    self.unit.hit(self.units_1[0])
                self.unit.action_points = 0
                self.unit.agred -= 1
            if self.unit.stunned > 0:
                self.unit.action_points = 0
                self.unit.stunned -= 1
        self.update_info()

    def next_round(self):
        """ This function passes the turn to another player, checking all the information about the character """
        self.turn = 0
        self.next_turn()
        for u in self.unit_order:
            u.hit_status = 1
            u.back_dmg = 0
            u.protection -= 1
            u.action_points = 3
            u.current_movement = u.movement
            u.current_damage = u.damage
            if u.cooldown1 > 0:
                u.cooldown1 -= 1
            if u.cooldown2 > 0:
                u.cooldown2 -= 1
            if u.cooldown3 > 0:
                u.cooldown3 -= 1
            if u.cooldown4 > 0:
                u.cooldown4 -= 1
        self.update_info()

    def set_allies(self):
        """ This function creates your characters """
        coords = []
        for i in range(self.N - 1):
            coords.append(i)
        self.units_1.append(
            Tank(100, 10, (self.N + 1) // 4, coords.pop(randint(0, self.N - 2)) * self.cell_size,
                 randint(self.N - 2, self.N - 1) * self.cell_size, 1, self.screen,
                 self.cell_size, self.cells))
        self.units_1.append(
            Rogue(60, 15, (self.N + 1) // 3, coords.pop(randint(0, self.N - 3)) * self.cell_size,
                  randint(self.N - 2, self.N - 1) * self.cell_size, 1, self.screen,
                  self.cell_size, self.cells))
        self.units_1.append(
            Wizard(55, 8, (self.N + 1) // 4, coords.pop(randint(0, self.N - 4)) * self.cell_size,
                   randint(self.N - 2, self.N - 1) * self.cell_size, 1, self.screen,
                   self.cell_size, self.cells))
        self.units_1.append(
            Sniper(60, 15, (self.N + 1) // 5, coords.pop(randint(0, self.N - 5)) * self.cell_size,
                   randint(self.N - 2, self.N - 1) * self.cell_size, 1, self.screen,
                   self.cell_size, self.cells))
        self.units_1.append(
            Support(70, 10, (self.N + 1) // 4, coords.pop(randint(0, self.N - 6)) * self.cell_size,
                    randint(self.N - 2, self.N - 1) * self.cell_size, 1, self.screen,
                    self.cell_size, self.cells))
        for i in range(5):
            self.cells[self.units_1[i].x // self.cell_size][self.units_1[i].y // self.cell_size - 1][2] = 1
        for i in self.units_1:
            i.draw_unit()

    def set_enemies(self):
        """ This function creates enemy characters """
        coords = []
        for i in range(self.N - 1):
            coords.append(i)
        self.units_2.append(
            Tank(100, 10, (self.N + 1) // 4, coords.pop(randint(0, self.N - 2)) * self.cell_size,
                 randint(1, 2) * (self.screen_height // (self.N + 1)), 2, self.screen,
                 self.cell_size, self.cells))
        self.units_2.append(
            Rogue(60, 15, (self.N + 1) // 3, coords.pop(randint(0, self.N - 3)) * self.cell_size,
                  randint(1, 2) * (self.screen_height // (self.N + 1)), 2, self.screen,
                  self.cell_size, self.cells))
        self.units_2.append(
            Wizard(55, 8, (self.N + 1) // 4, coords.pop(randint(0, self.N - 4)) * self.cell_size,
                   randint(1, 2) * (self.screen_height // (self.N + 1)), 2, self.screen,
                   self.cell_size, self.cells))
        self.units_2.append(
            Sniper(60, 15, (self.N + 1) // 5, coords.pop(randint(0, self.N - 5)) * self.cell_size,
                   randint(1, 2) * (self.screen_height // (self.N + 1)), 2, self.screen,
                   self.cell_size, self.cells))
        self.units_2.append(
            Support(70, 10, (self.N + 1) // 4, coords.pop(randint(0, self.N - 6)) * self.cell_size,
                    randint(1, 2) * (self.screen_height // (self.N + 1)), 2, self.screen,
                    self.cell_size, self.cells))
        for i in range(5):
            self.cells[self.units_2[i].x // self.cell_size][self.units_2[i].y // self.cell_size - 1][2] = 1
        for i in self.units_2:
            i.draw_unit()

    def use_ability(self, cell):
        """ This function allows you to use the abilities of heroes """
        aim = 0
        for unit in self.unit_order:
            if unit.x == cell[0] and unit.y == cell[1]:
                if self.unit.ability == 1:
                    self.unit.special_ability1(unit)
                if self.unit.ability == 2:
                    self.unit.special_ability2(unit)
                if self.unit.ability == 3:
                    self.unit.special_ability3(unit)
                if self.unit.ability == 4:
                    self.unit.special_ability4(unit)
                aim += 1
                if unit.current_hp <= 0:
                    self.unit_death(unit)
        if aim == 0:
            if self.unit.ability == 1:
                self.unit.special_ability1(cell)
            if self.unit.ability == 2:
                self.unit.special_ability2(cell)
            if self.unit.ability == 3:
                self.unit.special_ability3(cell)
            if self.unit.ability == 4:
                self.unit.special_ability4(cell)
