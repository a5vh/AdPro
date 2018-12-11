import pygame, sys, random, math

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Moving Cirle")
screen.fill((0,0,0))


while True:
    vel_x = .5
    vel_y = .5
    pos_x = random.randint(0,600)
    pos_y = random.randint(0,500)



        #MOVE CIRCLE
    pos_x += vel_x
    pos_y += vel_y

        #KEEP CIRCLE
    if pos_x > 400 or pos_x < 0:
        vel_x = -vel_x

    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y

    pos = 0,0

    color = 0,200,200
    pygame.draw.circle(screen, color, pos, 2, 1)

    pygame.display.update()
