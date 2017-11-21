import pygame

class powerup:

	def __init__(self, position, effect):
		self.position = position
		self.effect = effect
		self.size = 24

	def draw(self):
		if self.effect == "life":
			self.draw_life()
		elif self.effect == "blaster":
			self.draw_blaster()

	def draw_life(self):
		pos = self.position
		pygame.draw.rect(screen, (180,180,180), (pos[0]-11, pos[1]-11, 22, 22), 0)
		pygame.draw.rect(screen, (102,102,102), (pos[0]-12, pos[1]-12, 24, 24), 4)
		pygame.draw.line(screen, (255,42,42), (pos[0], pos[1]-8), (pos[0], pos[1]+8), 5)
		pygame.draw.line(screen, (255,42,42), (pos[0]-8, pos[1]), (pos[0]+8 ,pos[1]), 5)


	def draw_blaster(self):
		pos = self.position
		pygame.draw.rect(screen, (180,180,180), (pos[0]-11, pos[1]-11, 22, 22), 0)
		pygame.draw.rect(screen, (102,102,102), (pos[0]-12, pos[1]-12, 24, 24), 4)
		pygame.draw.line(screen, (255,42,42), (pos[0], pos[1]-9), (pos[0], pos[1]+9), 1)
		pygame.draw.line(screen, (255,42,42), (pos[0]-9, pos[1]), (pos[0]+9 ,pos[1]), 1)
		pygame.draw.circle(screen, (255,0,255), (pos[0]+1, pos[1]+1), 7, 1)

	def pickup(self):
		#get_effect()
		# Go away when player is in same position
		pass

	def get_effect(self):
		if self.effect =="life":
			player.lives +=1
		elif self.effect == "blaster":
			player.shot_freq *= 2


if __name__ == '__main__':
	screen = pygame.display.set_mode((800,600))
	pl = powerup((300,300), "life")
	pb = powerup((340,300), "blaster")
	while(True):
		pl.draw()
		pb.draw()
		pygame.display.flip()
