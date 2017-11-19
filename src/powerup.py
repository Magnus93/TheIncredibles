import pygame

class powerup:
	
	def __init__(self, position, effect):
	        self.position = position
	        self.effect = effect

        def draw_life(self,pos, color):
                pygame.draw.line(screen, color, pos, (pos[0],pos[1]+8),1)
                pygame.draw.line(screen, color, pos, (pos[0]+8,pos[1]),1)
                pygame.draw.line(screen, color, pos, (pos[0]-8,pos[1]),1)
                pygame.draw.line(screen, color, pos, (pos[0],pos[1]-8),1)
                pygame.draw.rect(screen, color, (pos[0]-12, pos[1]-12,24,24),2)

        def draw_blaster(self):
                pos = self.position
                self.draw_life(pos, (255,0,255))
                pygame.draw.circle(screen, (255,0,255), (pos[0]+1, pos[1]+1), 8, 1)

        def pickup(self): 
                #get_effect()
                # Go away when player is in same position
                pass

        def get_effect(self):
                if self.effect =="life":
                        player.lives +=1
                if self.effect == "blaster":
                        player.shot_freq *= 2


if __name__ == '__main__':
       screen = pygame.display.set_mode((800,600))
       p = powerup((300,300), "life")
       while(True):
        p.draw_life((400,400), (255, 0, 0))
        p.draw_blaster()
        pygame.display.flip()


