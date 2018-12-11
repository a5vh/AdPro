import pygame, sys
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Pong Game")
screen.fill((0,0,0))


class Fist(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""
def update(self):
        "move the fist based on the mouse position"
pos = pygame.mouse.get_pos()
self.rect.midtop = pos
if self.punching:
    self.rect.move_ip(5, 10)
width = 0
color = 255,255,255
pygame.draw.rect(screen, color, pos, width)
