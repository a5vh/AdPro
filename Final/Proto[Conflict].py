'''
Created on May 9, 2017

@author: 19augusthummert
'''
import pygame,sys, time, random, math
from MyLibrary import * 
class Player(pygame.sprite.Sprite):
    global bullet
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.direction = 0
        self.velocity = Point(0.0,0.0)
        self.rotation = 0.0 #degrees #added
        self.old_rotation = 0.0 #added
        
    def _getx(self): return self.rect.x
    
    def _gety(self): return self.rect.y
    
    def _getpos(self): return self.rect.topleft
    
    def load(self, filename, width=0, height=0, columns=1):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.set_image(self.master_image, width, height, columns)
    
    def update(self, current_time, rate=30):
        if self.last_frame > self.first_frame:
            #update animation frame number
            if current_time > self.last_time + rate:
                self.frame += 1
                if self.frame > self.last_frame:
                    self.frame = self.first_frame
                self.last_time = current_time
        else:
            self.frame = self.first_frame
            
    def draw(self, surface):
        surface.blit(self.image, (self.X,self.Y))
        
    def shoot(self):
        global laser
        all_sprites.add(laser)
        
        
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        laser = Laser(self.rect.centerx, self.rect.top)
        laser_img = laser.load("laserGreen.png")
        pygame.sprite.Sprite.__init__(self)
        self.image = laser_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill
    
    def load(self, filename, width=0, height=0, columns=1):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.set_image(self.master_image, width, height, columns)
                    
def game_init():
    global timer, player_group, player, font1, screen, playerx, font, laser_img, laser
    
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    font1 = pygame.font.Font(None, 36)
    timer = pygame.time.Clock()
    font = pygame.font.Font(None, 18)
    
    
    player_group = pygame.sprite.Group()
    player = laser
    player.load("F5S2N.png")
    player.position = ((600, 600))
    player_group.add(player)
    
    
 
#playerx = 600
game_init()
game_over = False
score = 0
lives = 0
level = 0




while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    laser = Laser(self.rect.centerx, self.rect.top)
    
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
    
    
    
    screen.fill((0,0,0))
    player_group.draw(screen)

    
    
    pygame.display.update()