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



def print_text(font,x,y,text,color=(255,255,255)):
    imgText = font.render(text,True,color)
    screen.blit(imgText,(x,y))

def wrap_angle(angle):
    return angle % 360

pygame.init()
screen = pygame.display.set_mode((1280, 1280))
pygame.display.set_caption("Space Demo")
font = pygame.font.Font(None,18)

space = pygame.image.load("space1.png").convert_alpha()
planet = pygame.image.load("ds.png").convert_alpha()
width,height = planet.get_size()
ship = pygame.image.load("Tatooine.png").convert_alpha()
planet1 = pygame.image.load("coruscant.png").convert_alpha()
earth = pygame.image.load("earth.png").convert_alpha()

radius = 160
radius1 = 440
radius2 = 300

mouse_x = mouse_y = 0
mouse_down = mouse_up = 0

angle = 0.0
angle1 = 0.0
angle2 = 0.0

pos = Point(0,0)
old_pos = Point(0,0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()


    screen.blit(space,(0,0))
    screen.blit(planet, (560,440))

    angle = wrap_angle(angle + 1.43)
    pos.x = math.sin(math.radians(angle)) * radius
    pos.y = math.cos(math.radians(angle)) * radius

    angle1 = wrap_angle(angle1 + 1)
    pos.x1 = math.sin(math.radians(angle1)) * radius1
    pos.y1 = math.cos(math.radians(angle1)) * radius1
    
    angle2 = wrap_angle(angle2 + 1.2)
    pos.x2 = math.sin(math.radians(angle2)) * radius2
    pos.y2 = math.cos(math.radians(angle2)) * radius2


    #rotate the ship
    #delta_x = ( pos.x - old_pos.x )
    #delta_y = ( pos.y - old_pos.y )
    #rangle = math.atan2(delta_x, delta_y)
    
    #delta_x1 = ( pos.x1 - old_pos.x )
    #delta_y1 = ( pos.y1 - old_pos.y )
    #rangle1 = math.atan2(delta_x1, delta_y1)
    
    #draw the ship
    width2,height2 = ship.get_size()
    x = 630 + pos.x-width2//2
    y = 500 + pos.y-height2//2
    screen.blit(ship, (x,y))
    
    width3,height3 = planet1.get_size()
    x1 = 630 + pos.x1-width3//2
    y1 = 500 + pos.y1-height3//2
    screen.blit(planet1, (x1,y1))
    
    width4,height4 = earth.get_size()
    x2 = 630 + pos.x2-width4//2
    y2 = 500 + pos.y2-height4//2
    screen.blit(earth, (x2,y2))

    #print_text(font,0,0,"Orbit: " + "{:.Of}".format(angle))
    #print_text(font,0,20,"Rotation: " + "{:.2f}".format(rangle))
    #print_text(font,0,40,"Position: " + str(pos))
    #print_text(font,0,60,"Old Pos: " + str(old_pos))

    pygame.display.update()

    #remember position
    old_pos.x = pos.x
    old_pos.y = pos.y
    
    old_pos.x1 = pos.x1
    old_pos.y1 = pos.y1
    
    old_pos.x2 = pos.x2
    old_pos.y2 = pos.y2