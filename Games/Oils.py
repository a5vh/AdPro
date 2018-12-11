'''
Created on Apr 6, 2017

@author: 19augusthummert
'''
import sys, time, random, math, pygame
from pygame.locals import * 
from MyLibrary import *

darktan = 190, 190, 110, 255
tan = 210, 210, 130, 255
skyblue = 135, 206, 250, 255


class OilSprite(MySprite):
    def __init__(self):
        MySprite.__init__(self)
        self.radius = random.randint(0,60) + 30
        play_sound(new_oil)
    
    def update(self, timing, rate=30):
        MySprite.update(self, timing, rate)    
    
    
    def fade(self):
        r2 = self.radius//2
        color = self.image.get_at((r2,r2))
        if color.a > 5:
            color.a -= 5
            pygame.draw.circle(self.image, color, (r2,r2) , r2, 0)
        else:
            oil_group.remove(self)
            play_sound(clean_oil)
            
            
def game_init():
    global screen, backbuffer, font, timer, oil_group, cursor, cursor_group
    
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Oil Spill Game")
    font = pygame.font.Font(None, 36)
    pygame.mouse.set_visible(False)
    timer = pygame.time.Clock()
    
    backbuffer = pygame.Surface((800,600))
    backbuffer.fill(skyblue)
    

    oil_group = pygame.sprite.Group()
    
    
    cursor = MySprite()
    cursor.radius = 80
    cursor.load("scrub.png", 200, 100, 1)

    '''image.fill((255,255,255,0))
    pygame.draw.circle(image, (80, 80, 220, 70), (30, 30), 30, 0)
    pygame.draw.circle(image, (80, 80, 250, 255), (30, 30), 30, 4)
    cursor.set_image(image)'''
    cursor_group = pygame.sprite.GroupSingle()
    cursor_group.add(cursor)
    
def audio_init():
    global new_oil, clean_oil
    
    new_oil = pygame.mixer.Sound("new_oil.wav")
    clean_oil = pygame.mixer.Sound("bubbles.wav")
    
def play_sound(sound):
    channel = pygame.mixer.find_channel(True)
    channel.set_volume(0.5)
    channel.play(sound)
    
def add_oil():
    global oil_group, new_oil
    
    oil = OilSprite()
    image = pygame.Surface((oil.radius,oil.radius)).convert_alpha()
    image.fill((255,255,255,0))
    oil.fadelevel = random.randint(50,150)
    oil_color = 231,254,255,oil.fadelevel
    r2 = oil.radius//2
    pygame.draw.circle(image, oil_color, (r2,r2), r2,0)
    oil.set_image(image)
    oil.X = random.randint(0,760)
    oil.Y = random.randint(0,560)
    oil_group.add(oil)
    play_sound(new_oil)
    
    
game_init()
audio_init()
last_time = 0

while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
        
        
    b1,b2,b3 = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos()
    pos = (mx+30, my+30)
    if b1 > 0:
        pygame.draw.circle(backbuffer, skyblue, pos, 30, 0)
        
        
    oil_hit = None
    for oil in oil_group:
        if pygame.sprite.collide_circle_ratio(0.5)(cursor, oil):
            oil_hit = oil
            if b1 > 0: oil_hit.fade()
            break
        
    if ticks > last_time + 1000:
        add_oil()
        last_time = ticks
        
        
    screen.blit(backbuffer, (0,0))
    
    
    oil_group.update(ticks)
    oil_group.draw(screen)
    
    
    cursor.position = (mx, my)
    cursor_group.update(ticks)
    cursor_group.draw(screen)
    
    if oil_hit: 
        print_text(font, 0, 0, "DIRTY BUBBLES - CLEAN THEM")
    else:
        print_text(font, 0,0, "CLEAN")
    pygame.display.update()