import pygame
import math

class bullet:
    def __init__(self, position, angle, color, surface):
        self.position = position
        self.angle = angle
        self.speed = 1.5
        self.color = color
        self.surface = surface

    def run(self):
        self.update_position()
        self.detect_collision()
        self.draw()

    def update_position(self):
        x_pos = (self.position[0] + self.speed*math.sin(self.angle))
        y_pos = (self.position[1] - self.speed*math.cos(self.angle))
        self.position = (x_pos, y_pos)

    def draw(self):
        pos = (int(self.position[0]), int(self.position[1]))
        pygame.draw.circle(self.surface, self.color, pos, 5, 2)
        pass

    def detect_collision(self):
        pass



if __name__ == '__main__':
    pass
