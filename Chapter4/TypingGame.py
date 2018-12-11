'''
Author: August Hummert
'''


import sys, random, time, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

def quit_game():
    sys.exit()

def reset_game():
    game_over = False
    seconds = 31
    clock_start = time.clock()
    
    
    
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("The Typing Game")
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 200)
white = 255,255,255
yellow = 255,255,255
correct_answer = 97
key_flag = False
seconds = 31
score = 0
clock_start = 0
game_over = True
hscore = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            key_flag = True
        elif event.type == KEYUP:
            key_flag = False
            if event.key == pygame.K_q:
                quit_game()
            if event.key == pygame.K_p:
                reset_game()
   
       
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    if keys[K_RETURN]:
        if game_over:
            game_over = False
            seconds = 31
            clock_start = time.clock()
    current = time.clock() - clock_start
    if seconds - current < 0:
        game_over = True
    elif current <= 30:
        if keys[correct_answer]:
            score += 1
            randomL = random.randint(1,8)
            if randomL == 1:#A
                correct_answer = 97
            if randomL == 2:#S
                correct_answer = 115
            if randomL == 3:#D
                correct_answer = 100
            if randomL == 4:#F
                correct_answer = 102
            if randomL == 5:#J
                correct_answer = 106
            if randomL == 6:#K
                correct_answer = 107
            if randomL == 7:#L
                correct_answer = 108
            if randomL == 8:#;
                correct_answer = 59
        elif keys [not correct_answer]:
            score -= 1
            randomL = random.randint(1,8)
            if randomL == 1:#A
                correct_answer = 97
            if randomL == 2:#S
                correct_answer = 115
            if randomL == 3:#D
                correct_answer = 100
            if randomL == 4:#F
                correct_answer = 102
            if randomL == 5:#J
                correct_answer = 106
            if randomL == 6:#K
                correct_answer = 107
            if randomL == 7:#L
                correct_answer = 108
            if randomL == 8:#;
                correct_answer = 59
            
            
                
            
    #Clear the screen
    screen.fill ((0, 100, 0))
    
    print_text(font1, 0, 50, "Lets Seee How Fast Your Fingers Are:")
    print_text(font1, 0, 100, "Try to keep up!")
    
    if key_flag:
        print_text(font1, 300, 50, "<key>")
        
    if not game_over:
        print_text(font1, 0, 150, "Time " + str(int(seconds-current)))
    
    print_text(font1, 0, 170, "Score = " + str(score))
    
    if game_over:
        print_text(font1, 0, 400, "Press Enter To Start....")
        if score > hscore:
            hscore = score
        print_text(font1, 0, 190, "High Score = " + str(hscore))
        print_text(font1, 0, 200, "Press Q to Quit or P to Play Again")

    
    

    
    print_text(font2, 0, 240, chr(correct_answer), yellow)
    
    pygame.display.update()