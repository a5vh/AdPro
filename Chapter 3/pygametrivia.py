'''
Created on Jan 24, 2017

@author: 19augusthummert
'''
import sys, pygame, math
from pygame.locals import *



class Trivia(object):
    def  __init__(self, filename):
        self.data = []
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white,white,white,white]
        self.qcount = 0
        
        
        
        #LOAD DATA FROM
        f = open(filename, "r")
        trivia_data = f.readlines()
        f.close()
        
        #COUNT AND CLEAN UP TRIVIA DATA
        for text_line in trivia_data:
            self.data.append(text_line.strip())
            self.total += 1
            
    def show_question(self):
        print_text(font1, 340, 5, "THE TECH QUIZ")
        if self.qcount < 10:
            #DISPLAY QUESTION
            question = self.current // 6 + 1
            print_text(font1, 5, 80, "QUESTION " + str(question))
            print_text(font2, 20, 120, self.data[self.current], yellow)
            print_text(font1, 5, 170, "ANSWERS")
            self.correct = int(self.data[self.current+5])
            print_text(font2, 20, 210, "1 - " + self.data[self.current+1], self.colors[0])
            print_text(font2, 20, 240, "2 - " + self.data[self.current+2], self.colors[1])
            print_text(font2, 20, 270, "3 - " + self.data[self.current+3], self.colors[2])
            print_text(font2, 20, 300, "4 - " + self.data[self.current+4], self.colors[3])
            print_text(font2, 190, 500-2, "Press keys 1-4 To Answer", white)
            print_text(font2, 600, 5,  "SCORE", white)
            print_text(font2, 600, 25, str(self.score), white)
            if self.scored:
                    self.colors = [white,white,white,white]
                    self.colors[self.correct-1] = green
                    print_text(font1, 250, 380, "CORRECT!", green)
                    print_text(font2, 190, 420, "Press Enter for Next Question", green)
            elif self.failed:
                    self.colors = [white,white,white,white]
                    self.colors[self.wronganswer-1] = red
                    self.colors[self.correct-1] = green
                    print_text(font1, 240, 380, "INCORRECT", red)
                    print_text(font2, 190, 420, "Press Enter for Next Question", red)
        else: 
            print_text(font1, 240, 270,"Press P to Play Again")
            print_text(font1, 240, 240,"Press Q to Quit the Game")
            trivia.show_score()
            
        
       

    def handle_input(self, number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 1
                
            else: 
                self.failed = True
                self.wronganswer = number
                
                
        
    def next_question(self):
        if self.qcount < 10 and (self.scored or self.failed):
            self.qcount += 1
            self.scored = False
            self.failed = False
            self.correct = 0
            self.colors = [white,white,white,white]
            self.current += 6
            #DISPLAY SCORE
            #ASK TO PLAY AGAIN OR QUIT 
            #MAKE METHODS QUIT/RESET
    def quit_game(self):
        sys.exit()

    def reset_game(self):
        self.current = 0
        self.total = 0
        self.correct = 0
        self.score = 0
        self.scored = False
        self.failed = False
        self.wronganswer = 0
        self.colors = [white,white,white,white]
        self.qcount = 1
        
    def show_score(self):
       
        print_text(font1, 240, 300,("Your score is...."  + str(self.score) + "0%"))
        
    
   

        
        #LOAD DATA FROM TRVIA.TXT
        

        #COUNT AND CLEAN UP TRIVIA DATA

                
   
            



def print_text(font,x,y, text, color=(255,255,255), shadow=True):
    if shadow:
        imgText = font.render(text, True, (0,0,0))
        screen.blit(imgText, (x-2,y-2))
        imgText = font.render(text,True,color)
        screen.blit(imgText, (x,y))
        
    
        
    #Main Program Begins
pygame.init()
screen = pygame.display.set_mode((720,500))
pygame.display.set_caption("The Trivia Game")
screen.fill((0,255,255))
font1 = pygame.font.Font(None,40)
font2 = pygame.font.Font(None,24)
white = 255,255,255
cyan = 0,255,255
yellow = 255,255,0
purple = 255,0,255
green = 0,255,0
red = 255,0,0

#Load Trivia Game
trivia = Trivia("trivia_data.txt")
    
    #Setup Keys
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:  
                trivia.handle_input(1)
            elif event.key == pygame.K_2:  
                trivia.handle_input(2)
            elif event.key == pygame.K_3:
                trivia.handle_input(3)
            elif event.key == pygame.K_4:
                trivia.handle_input(4)
            elif event.key == pygame.K_RETURN:
                trivia.next_question()
            elif event.key == pygame.K_q:
                trivia.quit_game()
            elif event.key == pygame.K_p:
                trivia.reset_game()
   
    #Clear Screen
    
    screen.fill((0,0,200))
    
    #Display trivia data
    trivia.show_question()
    
    #Update Display
    pygame.display.update()
    
            
              
        
            
            
            
            