'''
Created on Apr 5, 2017

@author: 19augusthummert
'''
import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *


levels = (
(1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,0,0,1,1,1,1,1,
 1,1,1,1,1,0,0,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1),
          
(2,2,2,2,2,2,2,2,2,2,2,2,
 2,0,0,2,2,2,2,2,2,0,0,2,
 2,0,0,2,2,2,2,2,2,0,0,2,
 2,2,2,2,2,2,2,2,2,2,2,2,
 2,2,2,2,2,2,2,2,2,2,2,2,
 2,2,2,2,2,2,2,2,2,2,2,2,
 2,2,2,2,2,2,2,2,2,2,2,2,
 2,0,0,2,2,2,2,2,2,0,0,2,
 2,0,0,2,2,2,2,2,2,0,0,2,
 2,2,2,2,2,2,2,2,2,2,2,2),
          
(3,3,3,3,3,3,3,3,3,3,3,3,
 3,3,0,0,0,3,3,0,0,0,3,3,
 3,3,0,0,0,3,3,0,0,0,3,3,
 3,3,0,0,0,3,3,0,0,0,3,3,
 3,3,3,3,3,3,3,3,3,3,3,3,
 3,3,3,3,3,3,3,3,3,3,3,3,
 3,3,0,0,0,3,3,0,0,0,3,3,
 3,3,0,0,0,3,3,0,0,0,3,3,
 3,3,0,0,0,3,3,0,0,0,3,3,
 3,3,3,3,3,3,3,3,3,3,3,3),
)

def goto_next_level():
    global level, levels
    level += 1
    if level > len(levels)-1: level = 0
    load_level()
    
def update_blocks():
    global block_group, waiting
    if len(block_group) == 0:
        goto_next_level()
        waiting = True
    block_group.update(ticks,50)

def load_level():
    global level, block, block_image, block_group, levels, triggered, multiball, multiball_group
    
    block_image = pygame.image.load("blocks.png").convert_alpha()
    
    block_group.empty()
    
    for bx in range(0,12):
        for by in range(0,10):
            block = MySprite()
            block.set_image(block_image, 58, 28, 4)
            x = 40 + bx * (block.frame_width+1)
            y = 60 + by * (block.frame_height+1)
            block.position = x,y 
            
            
            num = levels[level][by*12+bx]
            block.first_frame = num-1
            block.last_frame = num-1
            if num > 0:
                block_group.add(block)
                
        print(len(block_group))
    if triggered: triggered = False
    
    for n in range (0,3):
        multiball = MySprite()
        multiball.load("ball2.png")
        multiball.position = paddle.X + 40, paddle.Y - 20
        multiball_group.add(multiball)
        
        
def game_init():
    global screen, font, timer
    global paddle_group, block_group, ball_group
    global paddle, block_image, block, ball
    global multiball, multiball_group, triggered, powerup_group, powerup
    
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Block Breaker Game")
    font = pygame.font.Font(None, 36)
    pygame.mouse.set_visible(False)
    timer = pygame.time.Clock()
    triggered = False
    
    #
    paddle_group = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    ball_group = pygame.sprite.Group()
    multiball_group = pygame.sprite.Group()
    powerup_group = pygame.sprite.Group()
    
    
    paddle = MySprite()
    paddle.load("paddle.png")
    paddle.position = 400, 540
    paddle_group.add(paddle) 
    
    
    ball = MySprite()
    ball.load("ball.png")
    ball.position = 400, 450
    ball_group.add(ball)
    
    multiball_image = pygame.image.load("ball2.png")
    
    powerup = MySprite()
    powerup.load("powerup.png")
    powerup.position = 400, 500
    powerup_group.add(powerup)
    
    
def move_paddle():
        global movex,movey,keys,waiting
        
        paddle_group.update(ticks, 50)
        
        if keys[K_SPACE]:
            if waiting:
                waiting = False
                reset_ball()
        elif keys[K_LEFT]: paddle.velocity.x = -10.0
        elif keys[K_RIGHT]: paddle.velocity.x = 10.0
        else:
            if movex < -2: paddle.velocity.x = movex
            elif movex > 2: paddle.velocity.x = movex
            else: paddle.velocity.x = 0
        
        paddle.X += paddle.velocity.x
        if paddle.X < 0: paddle.X = 0
        elif paddle.X > 710: paddle.X = 710

def reset_ball():
    ball.velocity = Point(4.5, -7.0)
    for b in multiball_group:
        b.velocity = Point(4.5, -7.0)
    
def move_ball():
    global waiting, ball, game_over, lives
    
    powerup_group.update(ticks, 50)
    ball_group.update(ticks, 50)
    if waiting:
        ball.X = paddle.X + 40
        ball.Y = paddle.Y - 20
    ball.X += ball.velocity.x
    ball.Y += ball.velocity.y
    if ball.X < 0:
        ball.X = 0
        ball.velocity.x *= -1
    elif ball.X > 780:
        ball.X = 780
        ball.velocity.x *= -1
    if ball.Y < 0:
        ball.Y = 0
        ball.velocity.y *= -1
    elif ball.Y > 580:
        waiting = True
        lives -= 1
        if lives < 1: game_over = True
        
def move_multiball():
    global triggered, multiball_group
    
    multiball_group.update(ticks, 50)
   #if triggered:
    for b in multiball_group:
        b.X += b.velocity.x
        b.Y += b.velocity.y
        if b.X < 0:
            b.X = 0
            b.velocity.x *= -1
        elif b.X > 780:
            b.X = 780
            b.velocity.x *= -1
        if b.Y < 0:
            b.Y = 0
            b.velocity.y *= -1
        elif b.Y > 580:
            multiball_group.remove(b)
        multiball_group.update(ticks, 50)

def collision_multiball_paddle():
    global triggered, multiball_group, paddle
    
    if triggered:
        for b in multiball_group:
            if pygame.sprite.collide_circle(b, paddle):
                b.velocity.y = -abs(b.velocity.y)
                b.bx = b.X + 8
                b.by = b.Y + 8
                b.px = paddle.X + paddle.frame_width/2
                b.py = paddle.Y + paddle.frame_height/2
                if b.bx < b.px:
                    b.velocity.x = -abs(b.velocity.x)
                else:
                    b.velocity.x = abs(b.velocity.x)

def collision_ball_paddle():
    if pygame.sprite.collide_rect(ball, paddle):
        ball.velocity.y = -abs(ball.velocity.y)
        bx = ball.X + 8
        by = ball.Y + 8
        px = paddle.X + paddle.frame_width/2
        py = paddle.Y + paddle.frame_height/2
        if bx < px:
            ball.velocity.x = -abs(ball.velocity.x)
        else:
            ball.velocity.x = abs(ball.velocity.x)


def collision_ball_blocks():
    global score, block_group, ball
    
    hit_block = pygame.sprite.spritecollideany(ball, block_group)
    if hit_block != None:
        score += 10
        block_group.remove(hit_block)
        bx = ball.X + 8
        by = ball.Y + 8
        
        
        if bx > hit_block.X+5 and bx < hit_block.X + hit_block.frame_width-5:
            if by < hit_block.Y + hit_block.frame_width/2:
                ball.velocity.y = -abs(ball.velocity.y)
            else:
                ball.velocity.y = abs(ball.velocity.y)
                
                
        elif bx < hit_block.X + 5:
            ball.velocity.x = -abs(ball.velocity.x)
        
        elif bx > hit_block.X + hit_block.frame_width - 5:
            ball.velocity.x = abs(ball.velocity.x)
        
        
        else:
            ball.velocity.y *= -1
            
def collision_ball_powerup():
    global powerup, block_group, ball, powerup_group, triggered, ticks
    hit_powerup = None
    hit_powerup = pygame.sprite.spritecollideany(ball, powerup_group)
    if hit_powerup != None:
        if pygame.sprite.collide_rect_ratio(0.5)(ball, hit_powerup):
            triggered = True
            powerup_group.update(ticks, 50)
        else: hit_powerup = None
            
def collision_multiball_blocks():
    global score, block_group, multiball_group, triggered
    
    if triggered:
        for b in multiball_group:
            hit_block = pygame.sprite.spritecollideany(b, block_group)
            if hit_block != None:
                score += 10
                block_group.remove(hit_block)
                b.bx = b.X + 8
                b.by = b.Y + 8
                
                
                if b.bx > hit_block.X+5 and b.bx < hit_block.X + hit_block.frame_width-5:
                    if b.by < hit_block.Y + hit_block.frame_width/2:
                        b.velocity.y = -abs(b.velocity.y)
                    else:
                        b.velocity.y = abs(b.velocity.y)
                        
                        
                elif b.bx < hit_block.X + 5:
                    b.velocity.x = -abs(b.velocity.x)
                
                elif b.bx > hit_block.X + hit_block.frame_width - 5:
                    b.velocity.x = abs(b.velocity.x)
                
                
                else:
                    b.velocity.y *= -1
            
            else: hit_block = None



game_init()
game_over = False
waiting = True
score = 0
lives = 3
level = 0
triggered = False
load_level()

while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    
    
    
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        elif event.type == MOUSEMOTION:
            movex,movey = event.rel
        elif event.type == MOUSEBUTTONUP:
            if waiting:
                waiting = False
                reset_ball()
        elif event.type == KEYUP:
            if event.key == K_RETURN:
                goto_next_level()
    
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()
    
    
    if not game_over:
        update_blocks()
        move_paddle()
        move_ball()
        collision_ball_powerup()
        move_multiball()
        collision_ball_paddle()
        collision_multiball_paddle()
        collision_ball_blocks()
        collision_multiball_blocks()
    
    screen.fill((50,50,100))
    block_group.draw(screen)
    ball_group.draw(screen)
    if triggered:
        multiball_group.draw(screen)
    else:
        powerup_group.draw(screen)
        
    paddle_group.draw(screen)
    
    print_text(font, 0, 0, "SCORE " + str(score))
    print_text(font, 200, 0, "LEVEL " + str(level+1))
    print_text(font, 400, 0, "BLOCKS " + str(len(block_group)))
    print_text(font, 670, 0, "BALLS  " + str(lives))
    if game_over:
        print_text(font, 300, 380, "G A M E  O V E R")
    pygame.display.update()