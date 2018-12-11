'''
Created on Feb 16, 2017

@author: 19augusthummert
'''

import math, pygame, sys, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Circle Test")
screen.fill((0,0,100))

pos_x = 300
pos_y = 250
radius = 100
angle = 360
color1 = 255,255,255

while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
        
    angle += .1
    if angle >= 360:
        angle = 0
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = r,g,b
        
    x = math.cos(math.radians(angle) ) * radius
    y = math.sin(math.radians(angle) ) * radius
    
    x1 = math.cos(math.radians(angle) ) * radius
    y1= math.sin(math.radians(angle) ) * radius
    
    pos = (int(pos_x + x), int(pos_y + y) )
    pos1 = (int(pos_x + x1), int(pos_y + y1) )
    pygame.draw.circle(screen, color, pos, 10 , 0)
    pygame.draw.circle(screen, color1, pos1, 5 , 0)
    
    pygame.display.update()