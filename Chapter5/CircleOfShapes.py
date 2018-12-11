#main program begins
import sys, random, math, pygame, time
from pygame.locals import *


def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
def wrap_angle(angle):
    return angle % 360



pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Analog Clock Demo")
font = pygame.font.Font(None, 36)

orange = 220,180,0
white = 255,255,255
yellow = 255,255,0
pink = 255,100,100
blue = 0, 255, 255
green = 0, 255, 0
red = 255, 0 ,0 

r = random.randint(0,255)
b = random.randint(0,255)
g = random.randint(0,255)
color = r, g, b


pos_x = 300
pos_y = 250
radius = 250
angle = 360


#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

   
    
    screen.fill((255,255,255))

    
    angle += 30
    
    if angle >= 360:
        angle = 0
    x = math.cos(math.radians(angle-10) ) * (radius-20)
    y = math.sin(math.radians(angle-10) ) * (radius-20)
    shapes = random.randint(1,4)
    if shapes == 1:
        pygame.draw.ellipse(screen, color, (int(pos_x + x), int(pos_y + y), 50, 100), 0)
        time.sleep(0.25)
    if shapes == 2:
        pygame.draw.rect(screen, color, (int(pos_x + x), int(pos_y + y), 100, 100), 0)
        time.sleep(0.25)
    if shapes == 3:
        pygame.draw.ellipse(screen, color, (int(pos_x + x), int(pos_y + y), 100, 50), 0)
        time.sleep(0.25)
    if shapes == 4:
        pygame.draw.rect(screen, color, (int(pos_x + x), int(pos_y + y), 75, 50), 0)
        time.sleep(0.25)
    

       
    #cover the center
   
    

    pygame.display.update()   

