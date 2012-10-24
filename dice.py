import random

class Dice(object):
	sides = [0,0,0,0,0,0]
	def __init__(self):
		pass
		
	def roll(self):
		random.seed()
		return self.sides[random.randrange(0,6)]


class GreenDice(Dice):
	def __init__(self):
		"1 = brain, 2 = run away, 3 = shotgun"
		self.sides = [1,1,1,2,2,3]
		self.d_name = "Green Dice"
		
class YellowDice(Dice):
	def __init__(self):
		"1 = brain, 2 = run away, 3 = shotgun"
		self.sides = [1,1,2,2,2,3]
		self.d_name = "Yellow Dice"

class RedDice(Dice):
	def __init__(self):
		"1 = brain, 2 = run away, 3 = shotgun"
		self.sides = [1,2,2,2,3,3]
		self.d_name = "Red Dice"