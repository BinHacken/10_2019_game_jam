#-----Imports-----
import pygame
from pygame.locals import *
from character import character
#-----Initialization-----
pygame.init()
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Game1")
world_gravity = 0.009

#-----Character Creation-----
char = character(20, 20, 15, 20, 0.5, 0, 2)

clock = pygame.time.Clock()
run = True
#-----Main Game Loop-----
while run:
    #-----Frame rate limiter-----
    time_since_last_frame = clock.tick(60)
    #-----Event collection-----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    #-----Character Update-----
    char.update(keys, world_gravity, window.get_size(), time_since_last_frame)
    #-----Drawing the frame-----
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (char.x, char.y, char.width, char.height))
    pygame.display.update()
#-----Quit properly-----
pygame.quit()
