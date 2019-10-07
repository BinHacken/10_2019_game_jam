import pygame

class character:
    #----init gets caled on creation of object-----
    def __init__(self, x, y, width, height, speed, fall_speed, jump_strength):
        self.x  = x
        self.y  = y
        self.width  = width
        self.height  = height
        self.speed  = speed
        self.fall_speed = fall_speed
        self.jump_strength = jump_strength
        self.on_ground = False
    #-----Updates the character every frame-----
    def update(self, keys, world_gravity, world_size, time_since_last_frame):
        #-----Gravity-----
        self.y += self.fall_speed * time_since_last_frame
        if self.y + self.height > world_size[1]:
            self.fall_speed = 0
            self.on_ground = True
        else:
            self.fall_speed += world_gravity * time_since_last_frame
            self.on_ground = False
        #-----Player induced movement/key presses-----
        if keys[pygame.K_a] == True:
            self.x -= self.speed * time_since_last_frame
        if keys[pygame.K_d] == True:
            self.x += self.speed * time_since_last_frame
        if keys[pygame.K_SPACE] == True and self.on_ground == True:
            self.fall_speed = -self.jump_strength

        #-----Limiting the movement to the window-----
        if(self.y + self.height > world_size[1]):
            self.y = world_size[1] - self.height
        if(self.y  < 0):
            self.y = 0
        if(self.x + self.width > world_size[0]):
            self.x = world_size[0] - self.width
        if(self.x < 0):
            self.x = 0
