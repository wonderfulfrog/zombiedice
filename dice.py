import random


class Dice(object):
    "1 = brain, 2 = run away, 3 = shotgun"
    def __repr__(self):
        return self.d_name

    def roll(self):
        random.seed()
        return random.choice(self.sides)


class GreenDice(Dice):
    sides = [1, 1, 1, 2, 2, 3]
    d_name = "Green Dice"


class YellowDice(Dice):
    sides = [1, 1, 2, 2, 2, 3]
    d_name = "Yellow Dice"


class RedDice(Dice):
    sides = [1, 2, 2, 2, 3, 3]
    d_name = "Red Dice"
