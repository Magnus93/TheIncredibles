class Player: 
    def __init__player(self, player_id, position, color, name, lives, shot_freq):
        self.player_id = player_id
        self.position = position
        self.speed = (0,0)
        self.angle = 0
        self.angle_speed = 0
        
        self.color = color
        self.lives = 3
        
        self.shot_freq = shot_freq 
        self.name = name

    def update_position(self):
        pass

    def check_collision(self, other_player):
        pass

    def draw_player(self):
        pass
    
    def shoot(self):
        pass

    def die(self):
        pass

    def take_damage(self):
        self.lives -= 1
        if self.lives < 1:
            self.die()
        

