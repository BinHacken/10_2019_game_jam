#!/usr/bin/python3
#-----Imports-----
import pygame
from pygame.locals import *
#-----Initialization-----
pygame.init()
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Game1")
world_gravity = 0.009

#-----Character Data-----
character = {'x': 20, 'y': 20, 'width':15, 'height':20, 'move_speed':0.5, 'fall_speed': 0, 'jump_strength':2, 'on_ground': False}

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
    character['y'] += character['fall_speed'] * time_since_last_frame
    if character['y'] + character['height'] > window.get_size()[1]:
        character['fall_speed'] = 0
        character['on_ground'] = True
    else:
        character['fall_speed'] += world_gravity * time_since_last_frame
        character['on_ground'] = False
    #-----Player induced movement/key presses-----
    if keys[pygame.K_a] == True:
        character['x'] -= character['move_speed'] * time_since_last_frame
    if keys[pygame.K_d] == True:
        character['x'] += character['move_speed'] * time_since_last_frame
    if keys[pygame.K_SPACE] == True and character['on_ground'] == True:
        character['fall_speed'] = -character['jump_strength']

    #-----Limiting the movement to the window-----
    if(character['y'] + character['height'] > window.get_size()[1]):
        character['y'] = window.get_size()[1] - character['height']
    if(character['y']  < 0):
        character['y'] = 0
    if(character['x'] + character['width'] > window.get_size()[0]):
        character['x'] = window.get_size()[0] - character['width']
    if(character['x'] < 0):
        character['x'] = 0
    #-----Drawing the frame-----
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (character['x'], character['y'], character['width'], character['height']))
    pygame.display.update()
#-----Quit properly-----
pygame.quit()
