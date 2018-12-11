'''
Created on Feb 16, 2017

@author: 19augusthummert
'''
import sys, pygame, math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Bunches of Shapes")
font = pygame.font.Font(None,59)
orange = 255,69,0
white = 255,255,255
yellow = 218, 165, 32
pink = 255,100,100
green = 34, 139, 34
pos_x = 350
pos_y = 250
radius = 200
angle = 360
f = 1

while True:
    