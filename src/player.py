import pygame
import aux
import math

class player:
    def __init__(self, player_id, position, color, name):
        self.player_id = player_id
        self.position = position
        self.inpt = aux.create_input()
        self.boost = False
        self.thrust = 0.001
        self.speed = (0,0)
        self.angle = 0
        self.angle_speed = 0
        self.color = color
        self.lives = 3
        self.shot_freq = 2.0
        self.name = name

    def run(self):
        self.get_input()
        self.update_position()
        self.check_wall_collision()
        self.draw()

    def get_input(self):
        self.inpt.run()
        self.boost = self.inpt.up
        if self.inpt.left:
            print "LEft"
            self.angle_speed -= 0.00005
        if self.inpt.right:
            print "self.right"
            self.angle_speed += 0.00005

    def update_position(self):
        self.angle += self.angle_speed
        if self.boost:
            print "boost"
            x_speed = self.speed[0] + self.thrust*math.sin(self.angle)
            y_speed = self.speed[1] - self.thrust*math.cos(self.angle)
            self.speed = (x_speed, y_speed)
        x_pos = self.position[0] + self.speed[0]
        y_pos = self.position[1] + self.speed[1]
        self.position = (x_pos, y_pos)

        self.angle_speed *= 0.999
        self.speed = (0.9995*self.speed[0], 0.9995*self.speed[1])

    def check_wall_collision(self):
        if self.position[0] < 0 or self.position[0] > 600:
            self.speed = (-1*self.speed[0], self.speed[1])
            if self.position[0] < 0:
                self.position = (0, self.position[1])
            elif self.position[0] > 600:
                self.position = (600, self.position[1])
        if self.position[1] < 0 or self.position[1] > 600:
            self.speed = (self.speed[0], -1*self.speed[1])
            if self.position[1] < 0:
                self.position = (self.position[0], 0)
            elif self.position[1] > 600:
                self.position = (self.position[0], 600)

    def check_collision(self, other_player):
        pass

    def draw(self):
        if self.boost:
            shape = [(-3,6),(-5,12),(-2,9),(0,12),(2,9),(5,12),(3,6)]
            aux.draw_polygon(space, self.position, shape, self.angle, (255,255,0))
        shape = [(0,-10),(-5,6),(5,6)]
        aux.draw_polygon(space, self.position, shape, self.angle, self.color)

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
    space = pygame.Surface((600,600))
    p1 = player(1, (300,300), (255,0,255), "Nea")

    while True:
        screen.fill((26,26,26))
        space.fill((51,51,51))
        p1.run()
        screen.blit(space, (0,0))
        pygame.display.flip()
