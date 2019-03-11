import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *



def game_init():
    global screen, font, timer
    global snake_group, bit_group
    global snake, bit_image, bit

    pygame.init()
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption("Hello there")
    font = pygame.font.Font(None, 36)
    pygame.mouse.set_visible(False)
    timer = pygame.time.Clock()

    bit_group = pygame.sprite.Group()

    snake = MySprite()
    snake.load("Square.jpg", 10, 10, 1)
    snake.position = 400, 400



def load_menu():
    global keys
    keys = pygame.key.get_pressed()
    print_text(font, 400, 400, "Press P to Play")
    if keys[K_p]:
        load_game()

def load_game():
    pass

def move_snake():
    pass


game_init()
waiting = True
score = 0

while True:
    timer.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()

    screen.fill((250, 250, 250))

    snake.draw(screen)

    pygame.display.update()

