import pygame
from math import *

class player: 
    def __init__(self, player_id, position, color, name):
        self.player_id = player_id
        self.position = position
        self.speed = (0,0)
        self.angle = 0
        self.angle_speed = 0
        self.color = color
        self.lives = 3
        self.shot_freq = 2.0
        self.name = name

    def update_position(self):
        # Flytta ut icke position events
        for event in  pygame.event.get():
        #    if event.type == pygame.QUIT:
         #       print("quit")
            #Här funkar inte hold down key, nånting om att det bara läggs på queue?
            if event.type == pygame.KEYDOWN:
                pressed_key = pygame.key.get_pressed()
                if pressed_key[pygame.K_UP]:
                    print("UP")
                    self.position = (self.position[0], self.position[1]-1)
                if pressed_key[pygame.K_DOWN]:
                    print("down")
                    self.position = (self.position[0], self.position[1]+1)
                if pressed_key[pygame.K_LEFT]:
                    print("LEFT")
                    self.position = (self.position[0]-1, self.position[1])
                if pressed_key[pygame.K_RIGHT]:
                    print("RIGHT")
                    self.position = (self.position[0]+1, self.position[1])
        

    def check_collision(self, other_player):
        pass

    def draw(self):
        pygame.draw.circle(screen,self.color, self.position, 10) 
        
    def shoot(self):
        pass

    def die(self):
        pass

    def take_damage(self):
        self.lives -= 1
        if self.lives < 1:
            self.die()
        

if __name__ == '__main__':
    screen = pygame.display.set_mode((800,600))
    p1 = player(1, (20,30), (255,0,255), "Nea")
   
    while True:
        screen.fill((0,0,0))
        p1.draw()
        p1.update_position()
        pygame.display.flip()
