'''
Created on May 9, 2017

@author: 19augusthummert
'''
import pygame,sys, time, random, math
from MyLibrary import *
class Player():
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface
        


class Laser(MySprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill((255, 0 ,0))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -5

    def update(self):
        self.rect.y += self.speedy
        #kill
        if self.rect.bottom < 0:
            self.kill()


    def update(self,ticks):
        self.position.x += self.velocity.x * 10.0
        self.position.y += self.velocity.y * 10.0
        if self.position.x < 0 or self.position.x > 800 \
                or self.position.y < 0 or self.position.y > 600:
            self.alive = False
        self.rect = Rect(self.position.x, self.position.y, 4, 4)

    def draw(self,surface):
        pos = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(surface, self.color, pos, 4, 0)




def game_init():
    global timer, player_group, player, font1, screen, playerx, font, laser_img, laser, player_group, laser_group
    
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    font1 = pygame.font.Font(None, 36)
    timer = pygame.time.Clock()
    font = pygame.font.Font(None, 18)

    player = Player()
    player.load("F5S2N.png")
    player.fire_timer = 0
    player.position = 600,600
    player_group = pygame.sprite.Group()
    player_group.add(player)

    laser = Laser(player.X, player.Y)
    laser_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()


    
 
#playerx = 600
game_init()
game_over = False
score = 0
lives = 0
level = 0
RED = (255, 0 ,0)



while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    
    if not game_over:
        player_group.update(ticks,50)
    print_text(font, 0, 100, "Position")
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]: sys.exit()
    elif key[K_RIGHT]:
        player.X += 10
    elif key[K_LEFT]:
        player.X -= 10
    elif key[K_UP]:
        player.Y -= 10
    elif key[K_DOWN]:
        player.Y += 10

    if key[K_SPACE]:
        player.shoot()




    if player.X >= 1260:
        player.X = 1250
    if player.X <= -30:
        player.X = -20
    if player.Y >= 660:
        player.Y = 650
    if player.Y <= 460:
        player.Y = 470
    
    if lives == 0:
        you_win = True
        game_over = True

    player_group.update(ticks)
    laser_group.update(ticks, 50)
    
    screen.fill((0,0,0))
    player_group.draw(screen)

    
    
    pygame.display.update()