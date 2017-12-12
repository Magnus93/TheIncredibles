import pygame
import aux
import math
import bullet

pygame.font.init()
font = pygame.font.SysFont("monospace", 24)

class player:
    def __init__(self, player_id, position, color, name):
        self.id = player_id

        self.inpt = aux.create_input()      # create input to keeptrack of input values
        self.boost = False

        self.position = position            #     position
        self.speed = (0,0)                  #   d position/dt
        self.thrust = 0.03                  # d^2 position/dt^2     (acceleration)

        self.angle = 0                      #     angle
        self.angle_speed = 0                #   d angle/dt
        self.angle_acceleration = 0.003     # d^2 angle/dt^2

        self.color = color
        self.radius = 10            # radius for collision
        self.lives = 3
        self.bullet_freq = 2          # bullet frequency per secound
        self.bullets = []             # List all bullets flying from the player
        self.bullet_counter = 0       # Counter to make sure player does not bullet every frame
        self.name = name            # Name of player
        self.immortal = False          # self.immortal is Lock
        self.immortal_counter = 0


    def __str__(self):
        return "\n"+ str(self.id) + " " + self.name


    # Top function that runs all other functions
    def run(self, screen, space, sidebar):
        self.get_input()
        if self.lives > 0:
            self.update_position()
            self.check_wall_collision()
            self.draw(screen, space, sidebar)
        for s in self.bullets:
            s.run(space)
            pos = s.position
            if pos[0] < 0 or pos[1] < 0 or 600 < pos[0] or 600 < pos[1]:
                    self.bullets.remove(s)
                    del(s)
        #if self.immortal:
         #   self.immortal_counter -= 1
        #if self.immortal_counter == 0:
         #   self.immortal = False

    def get_input(self):
        self.inpt.run()
        self.boost = self.inpt.up
        if self.inpt.left:
            self.angle_speed -= self.angle_acceleration
        if self.inpt.right:
            self.angle_speed += self.angle_acceleration
        if self.inpt.spacebar:
            self.bullet_counter += 1
            if self.bullet_counter%(60/self.bullet_freq) == 1:
                self.shoot()

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

    def draw(self, screen, space, sidebar):
        self.pos = (int(self.position[0]), int(self.position[1]))
        pygame.draw.circle(space, (70,70,70), self.pos, self.radius, 1)
        if self.boost:
            shape = [(-3,6),(-5,12),(-2,9),(0,12),(2,9),(5,12),(3,6)]
            aux.draw_polygon(space, self.position, shape, self.angle, (255,255,0))
        shape = [(0,-10),(-5,6),(5,6)]
        aux.draw_polygon(space, self.position, shape, self.angle, self.color)
        aux.draw_polygon(space, self.position, shape, self.angle, (255,255,255), 1)
        self.draw_player_stats(sidebar, (0, self.id*50))
        for b in self.bullets:
            b.draw(space)

    def draw_player_stats(self, surface, pos):
        name_text = font.render(self.name, 1, self.color)
        surface.blit(name_text, pos)
        lives_string = "* "*self.lives
        lives_text = font.render(lives_string, 1, self.color)
        surface.blit(lives_text, (pos[0], pos[1]+24))
        # powerups maybe?
        pass

    def shoot(self):
        s = bullet.bullet(self.position, self.angle, self.color)
        self.bullets.append(s)

    def die(self):
        self.position = (-10,0)

    #def take_damage(self):
    #    # Lock must be set on server
    #    # self.immortal is Lock
    #    self.immortal = True
    #    self.immortal_counter = 60
    #    self.lives -= 1
    #    if self.lives < 1:
    #        self.die()

    #def check_hit_from_other(self, other_player):
    #    player_pos = self.position
    #    for bullet in other_player.bullets:
    #        bullet_pos = bullet.position
    #        if player_pos[0]-self.radius < bullet_pos[0] < player_pos[0]+self.radius:
    #            if player_pos[1]-self.radius < bullet_pos[1] < player_pos[1]+self.radius:
    #                if not self.immortal:
    #                    other_player.bullets.remove(bullet)
    #                    self.take_damage()
    #                    return True
    #    return False
#
#    #def check_collision(self, other_player):
#    #    x_distance = self.position[0] - other_player.position[0]
#    #    y_distance = self.position[1] - other_player.position[1]
#    #    distance = math.sqrt(x_distance**2 + y_distance**2)
#    #    if distance < self.radius+other_player.radius:
#    #        tmp_speed = self.speed
#    #        self.speed = other_player.speed
#    #        other_player.speed = tmp_speed
#    #        self.take_damage()
#    #        other_player.take_damage()
#    #        return True
    #    return False



if __name__ == '__main__':
    screen = pygame.display.set_mode((800,600))         # Entire window
    space = pygame.Surface((600,600))                   # Area for flying around
    sidebar = pygame.Surface((200,600))
    p1 = player(1, (300,300), (255,0,255), "Nea")       # Create player
    p2 = player(2, (200,300), (255,0,0), "Arne")
    mytimer = pygame.time.Clock()                       # Create Clock

    while True:
        screen.fill((26,26,26))
        space.fill((51,51,51))
        sidebar.fill((26,26,26))

        p1.run(screen,space,sidebar)                    # Run everyting with player (draw, calc pos, collision etc.)
        p2.run(screen,space,sidebar)



        if p2.check_hit_from_other(p1):
            print("Apapapapapap")

        if p1.check_collision(p2):
            print("Collided with otter fucker")

        screen.blit(space, (0,0))
        screen.blit(sidebar, (600,0))

        mytimer.tick(60)                            # Keep while loop at 60 loops/sec
        pygame.display.flip()                       # Update screen
