'''
Created on Feb 10, 2017

@author: 19augusthummert
'''
import sys, pygame, math, time, random
from pygame import *


def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Bomb Catcher Game")
font1 = pygame.font.Font(None,24)
pygame.mouse.set_visible(False)
white = 255,255,255
red = 220,50,50
yellow = 230,230,50
black = 0,0,0
lives = 3
score = 0
game_over = True
mouse_x = mouse_y = 0

pos_x = 300
pos_y = 460

pos_x1 = 300
pos_y1 = 460

bomb_x = random.randint(0,500)
bomb_x1 = random.randint(0,500)
bomb_y = -50
bomb_y1 = -50

flash = False
flash1 = False
flashT = 0
flashT1 = 0
start = 90
end = 180

vel_y = 1
vel_x = .3
vel_y1 = 1
vel_x1 = .3

while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos 
            move_x,move_y = event.rel
        elif event.type == MOUSEBUTTONUP:    
            if game_over:
                game_over = False
                lives = 3
                score = 0
    keys = pygame.key.get_pressed()
    
    
    
    if keys[K_ESCAPE]:
        sys.exit()
   
    
    if score < 50:
        vel_y = 0.4
    if score > 50:
        vel_y = 0.6
    if score > 100:
        vel_y = 0.8
    if score > 150:
        vel_y = 1    
    
     
    if score < 50:
        vel_y1 = 0.5
    if score > 50:
        vel_y1 = 0.7
    if score > 100:
        vel_y1 = 0.9
    if score > 150:
        vel_y1 = 1.1 
    
    if not flash:
        screen.fill((0,0,100))
    else:
        screen.fill((255, 0, 0))
        if flashT > 50:
            flash = False
            flashT = 0
        flashT += 1
        
    if not flash1:
        screen.fill((0,0,100))
    else:
        screen.fill((255, 0, 0))
        if flashT1 > 50:
            flash1 = False
            flashT1 = 0
        flashT1 += 1    
        
        
    
    if game_over:
        print_text(font1, 100, 200, "<ClICK TO PLAY>")
    else:
        bomb_y += vel_y
        bomb_y1 += vel_y1
    
    
        if bomb_y > 500:
            bomb_x = random.randint(0,500)
            bomb_y = -50 
            lives -= 1
            flash = True
            if lives == 0:
                game_over = True
            
                
        elif bomb_y > pos_y:
            if bomb_x > pos_x and bomb_x < pos_x + 120:
                score += 10
                bomb_x = random.randint(0,500)
                bomb_y = -50
                
        if bomb_y1 > 500:
            bomb_x1 = random.randint(0,500)
            bomb_y1 = -50 
            lives -= 1
            flash1 = True
            if lives == 0:
                game_over = True
            
                
        elif bomb_y1 > pos_y1:
            if bomb_x1 > pos_x1 and bomb_x1 < pos_x1 + 120:
                score += 10
                bomb_x1 = random.randint(0,500)
                bomb_y1 = -50
    
                
        pygame.draw.circle(screen,black, (int(bomb_x-4), int(bomb_y)-4),30,0)
        pygame.draw.circle(screen,yellow, (int(bomb_x), int(bomb_y)),30,0)
        pygame.draw.arc(screen, red, (int(bomb_x-10), int(bomb_y-50),50,50), start, end, 8)
        
        
        pygame.draw.circle(screen,black, (int(bomb_x1-4), int(bomb_y1)-4),30,0)
        pygame.draw.circle(screen,black, (int(bomb_x1), int(bomb_y1)),30,0)
        pygame.draw.arc(screen, red, (int(bomb_x1-10), int(bomb_y1-50),50,50), start, end, 8)
        
        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 500:
            pos_x = 500
            
        pygame.draw.rect(screen, black, (pos_x-4,pos_y-4,120,40),0)
        pygame.draw.rect(screen, red, (pos_x, pos_y,120,40),0)
        
    print_text(font1, 0, 0, "LIVES: " + str(lives))
    print_text(font1, 500, 0, "SCORE: " + str(score))
    
    pygame.display.update()
    
    
        
        
        
        
        