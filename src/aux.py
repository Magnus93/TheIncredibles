import pygame
import math


def draw_polygon(surface, pivot_pos, shape_list, rotation, color, width = 0):
    sin = math.sin(rotation)
    cos = math.cos(rotation)
    rotated_shape = []
    for pos in shape_list:
        x = pivot_pos[0] + pos[0]*cos - pos[1]*sin
        y = pivot_pos[1] + pos[0]*sin + pos[1]*cos
        rotated_shape.append((x,y))
    pygame.draw.polygon(surface, color, rotated_shape, width)


class create_input:
    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.spacebar = False


    def run(self):
        for event in  pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.up = True
                if event.key == pygame.K_DOWN:
                    self.down = True
                if event.key == pygame.K_LEFT:
                    self.left = True
                if event.key == pygame.K_RIGHT:
                    self.right = True
                if event.key == pygame.K_SPACE:
                    self.spacebar = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.up = False
                if event.key == pygame.K_DOWN:
                    self.down = False
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False
                if event.key == pygame.K_SPACE:
                    self.spacebar = False

if __name__ == '__main__':
    screen = pygame.display.set_mode((600,600))
    rot = 0.0
    inpt = create_input()

    while(True):
        inpt.run()
        if inpt.left:
            rot += 0.004
        if inpt.right:
            rot -= 0.004
        screen.fill((60,60,60))

        draw_polygon(screen, (300.0,40.0), [(0,-10),(-5,5),(5,5)], rot, (0,255,255))
        pygame.display.flip()
