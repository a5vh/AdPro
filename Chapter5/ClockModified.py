#main program begins
import sys, random, math, pygame
from pygame.locals import *
from datetime import datetime, date, time

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
def wrap_angle(angle):
    return angle % 360



pygame.init()
screen = pygame.display.set_mode((600,500))
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

numerals  = ["XII", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "X"]


#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

   
    
    screen.fill((255,255,255))

#draw one step around the circle


    
    

    #draw the clock numbers 1-12
    for n in range(0,12):
        angle = math.radians( n * (360/12) - 90 )
        x = math.cos( angle ) * (radius-20)-10
        y = math.sin( angle ) * (radius-20)-10
        print_text(font, pos_x+x, pos_y+y, str(numerals[n]), color)

    #get the time of day
    today = datetime.today()
    hours = today.hour % 12
    minutes = today.minute
    seconds = today.second



    #draw the hours hand
    hour_angle = wrap_angle( hours * (360/12) - 90 )
    hour_angle = math.radians( hour_angle )
    hour_x = math.cos( hour_angle ) * (radius-80)
    hour_y = math.sin( hour_angle ) * (radius-80)
    target = (pos_x+hour_x,pos_y+hour_y)
    pygame.draw.line(screen, color, (pos_x,pos_y), target, 25)



    #draw the minutes hand
    min_angle = wrap_angle( minutes * (360/60) - 90 )
    min_angle = math.radians( min_angle )
    min_x = math.cos( min_angle ) * (radius-60)
    min_y = math.sin( min_angle ) * (radius-60)
    target = (pos_x+min_x,pos_y+min_y)
    pygame.draw.line(screen, color, (pos_x,pos_y), target, 12)


    #draw the seconds hand
    sec_angle = wrap_angle( seconds * (360/60) - 90 )
    sec_angle = math.radians( sec_angle )
    sec_x = math.cos( sec_angle ) * (radius-40)
    sec_y = math.sin( sec_angle ) * (radius-40)
    target = (pos_x+sec_x,pos_y+sec_y)
    pygame.draw.line(screen, color, (pos_x,pos_y), target, 6)

    
    #shapes = random.randint(1,4)
    #if shapes == 1:
        #pygame.draw.ellipse(screen, color, pos, 1)
    #if shapes == 2:
        #pygame.draw.rect(screen, color, pos, 1)
    #if shapes == 3:
        #pygame.draw.rect(screen, color, pos, 1)
    #if shapes == 4:
        #pygame.draw.ellipse(screen, color, pos, 2)

    #cover the center
    pygame.draw.circle(screen, color, (pos_x,pos_y), 20)
    print_text(font, 0, 0, str(hours) + ":" + str(minutes) + ":" + str(seconds), color)
    
    

    pygame.display.update()

