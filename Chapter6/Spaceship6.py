'''
Created on Feb 23, 2017

@author: 19augusthummert
'''
import random, math, pygame, sys
from pygame.locals import *

#build points on screen
class Point(object):
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    #x property
    def getx(self):
        return self.__x
    def setx(self,x):
        self.__x = x
    x = property(getx,setx)
    
    #y property
    def gety(self):
        return self.__y
    def sety(self,y):
        self.__y = y
    y = property(gety,sety)
    
    #returns coordinates as string
    def __str__(self):
        return "{X:" + "{:.Of}".format(self.__x) + ",Y:" + "{:.Of}".format(self.__y) + "}"
    
def print_text(font,x,y,text,color=(255,255,255)):
    imgText = font.render(text,True,color)
    screen.blit(imgText,(x,y))
    
def wrap_angle(angle):
    return angle % 360

pygame.init()
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Space Demo")
font = pygame.font.Font(None,18)

space = pygame.image.load("space1.png").convert_alpha()
planet = pygame.image.load("ds.png").convert_alpha()
width,height = planet.get_size()
ship = pygame.image.load("mf.png").convert_alpha()

radius = 200
angle = 0.0
pos = Point(0,0)
old_pos = Point(0,0)
speed = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    if keys[K_EQUALS]:
        speed += 0.001
    if keys[K_MINUS]:
        speed -= 0.001
        
    screen.blit(space,(0,0))
    screen.blit(planet, (400-width/2,250-height/2))
    
    angle = wrap_angle(angle + 0.3 + speed)
    
    pos.x = math.sin(math.radians(angle)) * radius
    pos.y = math.cos(math.radians(angle)) * radius
    
    #rotate the ship
    delta_x = ( pos.x - old_pos.x )
    delta_y = ( pos.y - old_pos.y )
    rangle = math.atan2(delta_x, delta_y)
    rangled = wrap_angle( math.degrees(rangle))
    scratch_ship = pygame.transform.rotate(ship,rangled)
    
    #draw the ship
    width2,height2 = ship.get_size()
    x = 400 + pos.x-width2//2
    y = 250 + pos.y-height2//2
    screen.blit(scratch_ship, (x,y))
    
    #print_text(font,0,0, "Orbit: " + "{:.")
    #print_text(font,0,20,"Rotation: " + "{:.2f}".format(rangle))
    #print_text(font,0,40,"Position: " + str(pos))
    #print_text(font,0,60,"Old Pos: " + str(old_pos))
    
    pygame.display.update()
    
    #remember position
    old_pos.x = pos.x
    old_pos.y = pos.y