class powerup:
	
	def __init__powerup(self, position):
	self.position = position
	self.effect = None


class life(powerup):
	
	def __init__life(self, position):
		powerup(position)

	def effect(self, player):
		player.lives += 1

class blaster(powerup):

	def __init__blaster(self, position):
		powerup(position)

	def effect(self, player):
		player.shot_freq *= 2

