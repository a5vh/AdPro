'''
Created on Feb 9, 2017

@author: 19augusthummert
'''

import sys, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Mouse Clicks")
font1 = pygame.font.Font(None,24)
white = 255,255,255

mouse_x = mouse_y = 0
move_x = move_y = 0
mouse_down = mouse_up = 0
mouse_down_x = mouse_down_y = 0
mouse_up_x = mouse_up_y = 0
radius = 10
width = 10
color = 255,255,255

while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos 
            move_x,move_y = event.rel
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = event.button
            mouse_down_x,mouse_down_y = event.pos
        elif event.type == MOUSEBUTTONUP:    
            mouse_up = event.button
            mouse_up_x,mouse_up_y = event.pos
    
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
        
    if mouse_down == True:
        pygame.draw.circle(screen, color, (mouse_x, mouse_y), 10, 10)
    
    screen.fill((0,100,0))
    
    print_text(font1, 0,  0, "Mouse Events")
    print_text(font1, 0, 20, "Mouse Position: " + str(mouse_x) + "," + str(mouse_y))
    print_text(font1, 0, 40, "Mouse Relative: " + str(move_x) + "," + str(move_y))
    
    print_text(font1, 0, 60, "Mouse Button Down: " + str(mouse_down) + " at " 
               + str(mouse_down_x) + "," + str(mouse_down_y))

    print_text(font1, 0, 80, "Mouse Button Up: " + str(mouse_up) + " at " 
               + str(mouse_up_x) + "," + str(mouse_up_y))
    
    x,y = pygame.mouse.get_pos()
    print_text(font1, 0, 180, "Mouse Position: " + str(x) + "," + str(y))
    
    c1, c2, c3 = pygame.mouse.get_pressed()
    print_text(font1, 0, 200, "Mouse Buttons: " + str(c1) + "," + str(c2) + "," + str(c3))
    
    pygame.draw.circle(screen, color, (mouse_x, mouse_y), 2, 0)
    
    pygame.display.update()
    
    
     
    
    
    
    