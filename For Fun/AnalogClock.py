import math, sys, random, pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Circle Demo")
screen.fill((0,0,100))


pos_x = 300
pos_y = 250
radius = 200
angle = 360

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    angle += 1
    if angle >= 360:
        angle = 0
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = r,g,b

    x = math.cos( math.radians(angle ) ) * radius
    y = math.sin( math.radians(angle ) ) * radius

    pos = ( int (pos_x + x), int(pos_y + y) )
    pygame.draw.circle(screen, color, pos, 10, 0)


    for n in range(1,13):
        angle = math.radians( n * (360/12) - 90 )
        x = math.cos( angle ) * (radius-20) - 10
        y = math.sin( angle ) * (radius-20) - 10
        print(font, ps_x+x, pos_y+y, str(n))


    pygame.display.update()
