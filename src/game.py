import pygame
import sys
import player
#import client

pygame.font.init()
font = pygame.font.SysFont("monospace", 24)

class local_game:
	def __init__(self):
		self.screen = pygame.display.set_mode((800,600))
		self.space = pygame.Surface((600,600))                   # Area for flying around
		self.sidebar = pygame.Surface((200,600))
		self.mytimer = pygame.time.Clock()                       # Create Clock

	def run(self, player_list, my_id):
		self.screen.fill((26,26,26))
		self.space.fill((51,51,51))
		self.sidebar.fill((26,26,26))
		for p in player_list:
			if p.id == my_id:
				p.run(self.screen, self.space, self.sidebar)
				player_list[my_id] = p 
			else:
				p.draw(self.screen, self.space, self.sidebar)

		self.screen.blit(self.space, (0,0))
		self.screen.blit(self.sidebar, (600,0))
		self.mytimer.tick(60)                            # Keep while loop at 60 loops/sec
		pygame.display.flip()                       # Update screen

		return player_list



if __name__ == '__main__':
	g = local_game()
	p1 = player.player(0,(50,50), (250,0,0), "mage")
	p2 = player.player(1,(70,50), (0,250,0), "nea")
	p3 = player.player(2,(90,50), (0,0,250), "elvis")
	p_list = [p1,p2,p3]

	while(True):
		p_list = g.run(p_list, 0)
