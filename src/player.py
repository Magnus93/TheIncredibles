import pygame
import aux
import math


class player:
    def __init__(self, player_id, position, color, name):
        self.player_id = player_id

        self.inpt = aux.create_input()      # create input to keeptrack of input values
        self.boost = False

        self.position = position            #     position
        self.speed = (0,0)                  #   d position/dt
        self.thrust = 0.05                  # d^2 position/dt^2     (acceleration)

        self.angle = 0                      #     angle
        self.angle_speed = 0                #   d angle/dt
        self.angle_acceleration = 0.003     # d^2 angle/dt^2

        self.color = color
        self.radius = 10            # radius for collision
        self.lives = 3
        self.shot_freq = 2.0
        self.name = name

    # Top function that runs all other functions
    def run(self):
        self.get_input()
        if self.lives > 0:
            self.update_position()
            self.check_wall_collision()
            self.draw()

    def get_input(self):
        self.inpt.run()
        self.boost = self.inpt.up
        if self.inpt.left:
            self.angle_speed -= self.angle_acceleration
        if self.inpt.right:
            self.angle_speed += self.angle_acceleration

    def update_position(self):
        self.angle += self.angle_speed
        if self.boost:
            x_speed = self.speed[0] + self.thrust*math.sin(self.angle)
            y_speed = self.speed[1] - self.thrust*math.cos(self.angle)
            self.speed = (x_speed, y_speed)
        elif self.inpt.down:
            x_speed = self.speed[0] - 0.5*self.thrust*math.sin(self.angle)
            y_speed = self.speed[1] + 0.5*self.thrust*math.cos(self.angle)
            self.speed = (x_speed, y_speed)
        x_pos = self.position[0] + self.speed[0]
        y_pos = self.position[1] + self.speed[1]
        self.position = (x_pos, y_pos)

        self.angle_speed *= 0.95
        self.speed = (0.9995*self.speed[0], 0.9995*self.speed[1])

    def check_wall_collision(self):
        lower_limit = self.radius
        upper_limit = 600-self.radius
        if self.position[0] < lower_limit or self.position[0] > upper_limit:    # if player outside space
            self.speed = (-1*self.speed[0], self.speed[1])                      # negate speed in x-axis
            if self.position[0] < self.radius:                                  # if player at lower limit
                self.position = (lower_limit, self.position[1])                 # Move player to edge
            elif self.position[0] > upper_limit:
                self.position = (upper_limit, self.position[1])
        if self.position[1] < lower_limit or self.position[1] > upper_limit:
            self.speed = (self.speed[0], -1*self.speed[1])
            if self.position[1] < lower_limit:
                self.position = (self.position[0], lower_limit)
            elif self.position[1] > upper_limit:
                self.position = (self.position[0], upper_limit)

    def check_collision(self, other_player):
        pass

    def draw(self):
        self.pos = (int(self.position[0]), int(self.position[1]))
        pygame.draw.circle(space, (70,70,70), self.pos, self.radius, 1)
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
    screen = pygame.display.set_mode((800,600))         # Entire window
    space = pygame.Surface((600,600))                   # Area for flying around
    p1 = player(1, (300,300), (255,0,255), "Nea")       # Create player
    mytimer = pygame.time.Clock()                       # Create Clock

    while True:
        screen.fill((26,26,26))
        space.fill((51,51,51))
        p1.run()                    # Run everyting with player (draw, calc pos, collision etc.)
        screen.blit(space, (0,0))

        mytimer.tick(60)                            # Keep while loop at 60 loops/sec
        pygame.display.flip()                       # Update screen
