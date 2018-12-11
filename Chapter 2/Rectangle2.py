'''
Created on Jan 17, 2017

@author: 19augusthummert
'''
import pygame, sys, random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Shapes")

r1 = 0
g1 = 0
b1 = 0


r2 = 0
g2 = 0
b2 = 0

r3 = 0
g3 = 0
b3 = 0



pos_x = random.randint(0,500)
pos_y = random.randint(0,400)

pos_x1 = random.randint(0,500)
pos_y1 = random.randint(0,400)

pos_x2 = random.randint(0,500)
pos_y2 = random.randint(0,400)



sizex = random.randint(200,250)
sizey = random.randint(100,150)

sizex1 = random.randint(100,150)
sizey1 = random.randint(100,150)

sizex2 = random.randint(100,150)
sizey2 = random.randint(100,150)

vel_x = 3
vel_y = 3

vel_x1 = 3
vel_y1 = 3

vel_x2 = 3
vel_y2 = 3





while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0,0,0))

    #move the rectangle
    pos_x += vel_x
    pos_y += vel_y

    pos_x1 += vel_x1
    pos_y1 += vel_y1

    pos_x2 += vel_x2
    pos_y2 += vel_y2


    #keep the rectangle
    if pos_x > 400 or pos_x < 0:
        vel_x = -vel_x
        r1 = random.randint(0,255)
        g1 = random.randint(0,255)
        b1 = random.randint(0,255)
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y
        r1 = random.randint(0,255)
        g1 = random.randint(0,255)
        b1= random.randint(0,255)


    if pos_x1 > 500 or pos_x1 < 0:
        vel_x1 = -vel_x1
        r2 = random.randint(0,255)
        g2= random.randint(0,255)
        b2 = random.randint(0,255)
    if pos_y1 > 400 or pos_y1 < 0:
        vel_y1 = -vel_y1
        r2 = random.randint(0,255)
        g2 = random.randint(0,255)
        b2 = random.randint(0,255)


    if pos_x2 > 500 or pos_x2 < 0:
        vel_x2 = -vel_x2
        r3 = random.randint(0,255)
        g3 = random.randint(0,255)
        b3 = random.randint(0,255)
    if pos_y2 > 400 or pos_y2 < 0:
        vel_y2 = -vel_y2
        r3 = random.randint(0,255)
        g3 = random.randint(0,255)
        b3 = random.randint(0,255)


    #draw rect 1
    color = r1,g1,b1
    width = 0 #solid fill
    pos = pos_x, pos_y, sizex, sizey
    pygame.draw.rect(screen, color, pos, width)

   




    pygame.display.update()
