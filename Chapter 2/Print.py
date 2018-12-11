import sys, pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
width = 8
pygame.draw.line(screen, color, (100,100), width)