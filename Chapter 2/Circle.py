
'''
Created on Jan 10, 2017

@author: 19augusthummert
'''
import pygame, sys, random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Drawing Lines")
vel_x = .5
vel_y = .5
pos_x = random.randint(0,600)
pos_y = random.randint(0,500)
while True:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                sys.exit()


        screen.fill((0,200,0))

        pos_x += vel_x
        pos_y += vel_y


        if pos_x > 400 or pos_x < 0:
            vel_x = -vel_x

        if pos_y > 400 or pos_y < 0:
            vel_y = -vel_y



    #draw a circle
        color = (0,0,0)
        pygame.draw.circle(screen, color, [350,350], 50, 0)


        pygame.display.update()
