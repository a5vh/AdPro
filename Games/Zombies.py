'''
Created on Mar 9, 2017

@author: 19augusthummert
'''
import itertools, sys, time, random, math, pygame
from pygame.locals import * 
from MyLibrary import * 

def calc_velocity(direction, vel=1.0):
    velocity = Point(0,0)
    if direction == 0:
        velocity.y = -vel
    if direction == 2:
        velocity.x = vel
    if direction == 4:
        velocity.y = vel
    if direction == 6:
        velocity.x = -vel
    return velocity

def reverse_direction(sprite):
    if sprite.direction == 0:
        sprite.direction = 4
    elif sprite.direction == 2:
        sprite.direction = 6
    elif sprite.direction == 4:
        sprite.direction = 0
    elif sprite.direction == 6:
        sprite.direction = 2
        
pygame.init()
screen = pygame.display.set_mode((800,600))
font = pygame.font.Font(None, 36)
pygame.display.set_caption("Collision Demo")
timer = pygame.time.clock()
    
    
player_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
health_group = pygame.sprite.Group()


player = MySprite()
player.load("farmer.png", 96, 96, 8)
player.position = 80, 80
player.direction = 4
player_group.add(player)

zombie_image = pygame.image.load("zombie.png").conver_alpha()
for n in range(0,10):#N = Zombie    
    zombie = MySprite()
    zombie.load("zombie", 96, 96, 8)
    zombie.position = random.randint(0,700), random.randint(0,500)
    zombie.direction = random.randint(0,3) * 2
    zombie_group.add(zombie)

health = MySprite()
health.load("health.png", 32, 32, 1)
health.position = 400, 300
health_group.add(health)

game_over = False
player_moving = False
player_health = 100


while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys [K_ESCAPE]:
        sys.exit()
    elif keys[K_UP] or keys[K_w]:
        player.direction = 0
        player_moving = True
    elif keys[K_RIGHT] or keys[K_d]:
        player.direction = 2
        player_moving = True
    elif keys[K_DOWN] or keys[K_s]:
        player.direction = 4
        player_moving = True
    elif keys[K_LEFT] or keys[K_a]:
        player.direction = 6
        player_moving = True
    
    
