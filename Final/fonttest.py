'''
Created on May 8, 2017

@author: 19augusthummert
'''
import pygame, pyglet
from pygame.locals import *
from MyLibrary import *
pyglet.font.add_file('action_man.ttf')
action_man = pyglet.font.load('Action Man')
print_text(font, 300, 300, "Hi")