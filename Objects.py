class Unit:
    """
    Describes a unit
    """

    def __init__(self, hp, damage, movement, x, y):
        self.hp = hp
        self.damage = damage
        self.movement = movement
        self.x = x
        self.y = y

    def draw_unit(self):
        """

        :return:
        """

    def move_unit(self):
        """

        :return:
        """


class MeleeUnit(Unit):
    """

    """

    def __init__(self, hp, damage, movement, x, y):
        super().__init__(hp, damage, movement, x, y)

    def hit(self):
        """

        :return:
        """

    def special_ability(self):
        """

        :return:
        """


class RangeUnit(Unit):
    """

    """

    def __init__(self, hp, damage, movement, x, y):
        super().__init__(hp, damage, movement, x, y)

    def hit(self):
        """

        :return:
        """

    def special_ability(self):
        """

        :return:
        """


class Wall:
    """

    """

    x = 0

    y = 0

