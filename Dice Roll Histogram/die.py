
# Die class used to create dice of any number of sides for use with die_visual.py 
from random import randint

class Die:
	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		"""return a random value between 1 and number of sides"""
		return randint(1, self.num_sides)