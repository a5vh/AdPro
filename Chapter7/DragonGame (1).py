import pygame,sys,time,random,math
from pygame.locals import *


class MySprite(pygame.sprite.Sprite):
    def __init__(self,target):
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
        
    def _getx(self): return self.rect.x
    def _setx(self,value): self.rect.x = value
    x = property(_getx,_setx)
    
    def _gety(self): return self.rect.y
    def _sety(self,value): self.rect.y = value
    y = property(_gety,_sety)
    
    def _getpos(self): return self.rect.test_topleft
    def _setpos(self,pos): self.rect.topleft = pos
    position = property(_getpos,_setpos)
    
    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0,0,width,height)
        self.columns = columns
        
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width//width) * (rect.height//height) - 1
        
    def update(self, current_time, rate = 30):
        
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
        
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x,frame_y,self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame
            
    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
            "," + str(self.last_frame) + "," + str(self.frame_width) + \
            "," + str(self.frame_height) + "," + str(self.columns) + \
            "," + str(self.rect)
def print_text(font,x,y,text,color=(255,0,255)):
    imgText = font.render(text,True,color)
    screen.blit(imgText, (x,y))
    
def reset_fireball():
    y = random.randint(250,350)
    fireball.position = 1200,y
    
pygame.init()
screen = pygame.display.set_mode((1200,600),0,32)
pygame.display.set_caption("Animated Sprite Demo")
font = pygame.font.Font(None,18)
framerate = pygame.time.Clock()

group = pygame.sprite.Group()

space = pygame.image.load("space1.png").convert_alpha()

dragon = MySprite(screen)
dragon.load("dragon.png", 124, 58, 3)
dragon.position = 100,300
group.add(dragon)

smurf = MySprite(screen)
smurf.load("smurf.png", 128, 128, 4)
smurf.first_frame = 1
smurf.last_frame = 7
smurf.position = 400,300
group.add(smurf)


puma = MySprite(screen)
puma.load("puma.png", 256, 128, 2)
puma.first_frame = 1
puma.last_frame = 7
puma.position = 400,300
group.add(puma)

fireball = MySprite(screen)
fireball.load("explosion.png", 128, 128, 4)
fireball.position = 800,320
group.add(fireball)

fireball_vel = 8.0
game_over = False
you_win = False
smurf_jumping = False
puma_jumping = False
jump_vel = 0.0
jump_vel1 = 0.0
smurf_start_y = smurf.y
puma_start_y = puma.y
lives = 3
plives = 3
dlives = 3

while True:
    framerate.tick(30)
    ticks = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]: sys.exit()
    elif key[K_UP]:
        if not smurf_jumping:
            smurf_jumping = True
            jump_vel = -8.0
    elif key[K_RIGHT]:
        smurf.x += 5
    elif key[K_LEFT]:
        smurf.x -= 5
    
    
    elif key[K_w]:
        if not puma_jumping:
            puma_jumping = True
            jump_vel1 = -8.0
    elif key[K_a]:
        puma.x -= 5
    elif key[K_d]:
        puma.x += 5
            
    if not game_over:
        fireball.x -= fireball_vel
        if fireball.x < -40: reset_fireball()
        
    if pygame.sprite.collide_rect(fireball, smurf):
        reset_fireball()
        lives -= 1
        dlives += 1
        reset_fireball()
        
    if pygame.sprite.collide_rect(fireball, puma):
        plives -= 1
        dlives += 1
        reset_fireball()
    
    if pygame.sprite.collide_rect(fireball, dragon):
        reset_fireball()
        dlives -= 1
        
    if pygame.sprite.collide_rect(dragon, smurf):
        game_over = True
    
    if lives == 0 or plives == 0:
        you_win = False
        game_over = True
        
    if dlives == 0:
        you_win = True
        game_over = True
    
    if smurf_jumping:
        smurf.y += jump_vel - 7.0
        jump_vel += 0.5
        if smurf.y > smurf_start_y:
            smurf_jumping = False
            smurf.y = smurf_start_y
            jump_vel = 0.0
            
    if puma_jumping:
        puma.y += jump_vel1 - 7.0
        jump_vel1 += 0.5
        if puma.y > puma_start_y:
            puma_jumping = False
            puma.y = puma_start_y
            jump_vel1 = 0.0
    
    screen.fill((0,0,0))
    screen.blit(space,(0,0))
    print_text(font,230,90,"Smurf Lives Left: " + str(lives))
    print_text(font,530, 90,"Puma Lives Left: " + str(plives))
    print_text(font,830,90,"Dragon Lives Left: " + str(dlives))
    
    if not game_over:
        group.update(ticks,50)
        
    
    group.draw(screen)
    print_text(font,350,560,"Press Space To Jump")
    
    if game_over:
        print_text(font,330,110,"G A M E  O V E R")
        if you_win:
            print_text(font,330,130,"YOU BEAT THE DRAGON")
        else:
            print_text(font,330,130,"THE DRAGON GOT YOU")
    pygame.display.update()