# Pygame template - skeleton for a new pygame project
import pygame
import random
import sys
import time
from os import path
img_dir = path.join(path.dirname(__file__), 'Images')
snd_dir = path.join(path.dirname(__file__), 'Sounds')

WIDTH = 600
HEIGHT = 650
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
lives = 3

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygala")
clock = pygame.time.Clock()
font = pygame.font.Font("/Users/augusthummert/Google Drive/Code/Final/font1.ttf", 18)

def draw_text(font, surf, text, size, x , y):
    font = pygame.font.Font("/Users/augusthummert/Google Drive/Code/Final/font1.ttf", size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = player.shield
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_shield_bar2(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = player.shield
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, BLUE, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def show_go_screen():
    mmenu = True



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50,50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 25
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH /2
        self.rect.bottom = HEIGHT - 20
        self.speedx = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot =  pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()


    def update(self):
        #unhide if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.speedx = -10
        if keys[pygame.K_RIGHT]:
            player.speedx = 10

        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            laser = Laser(self.rect.centerx, self.rect.top)
            all_sprites.add(laser)
            lasers.add(laser)
            shoot_sound.play()

    def hide(self):
        #hide
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH /2, HEIGHT + 200)

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player2_img, (50,50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 25
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH /2
        self.rect.bottom = HEIGHT - 20
        self.speedx = 0
        self.shield2 = 100
        self.shoot_delay = 250
        self.last_shot =  pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()


    def update(self):
        #unhide if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speedx = -10
        if keys[pygame.K_d]:
            self.speedx = 10

        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            laser = Laser(self.rect.centerx, self.rect.top)
            all_sprites.add(laser)
            lasers.add(laser)
            shoot_sound.play()

    def hide(self):
        #hide
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH /2, HEIGHT + 200)

class Mob(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(enemy_images)
        self.image.set_colorkey(BLACK)
        self.rect = rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85/2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(3,9)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off top
        if self.rect.bottom < 0:
            self.kill()

class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = elaser_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off top
        if self.rect.bottom > 650:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center



# Load all Sprites

background = pygame.image.load(path.join(img_dir, "blue.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "playerShip2_orange.png")).convert()
player2_img = pygame.image.load(path.join(img_dir, "playerShip1_blue.png")).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player2_mini_img = pygame.transform.scale(player2_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
player2_mini_img.set_colorkey(BLACK)
laser_img = pygame.image.load(path.join(img_dir, "laserGreen.png")).convert()
elaser_img = pygame.image.load(path.join(img_dir, "laserRed.png")).convert()
enemy_images = []

enemy_list = ["enemyBlack1.png", "enemyBlack2.png", "enemyBlack3.png", "enemyBlack4.png", "enemyBlack5.png"]
for img in enemy_list:
    enemy_images.append(pygame.image.load(path.join(img_dir, img)).convert())
#Load All Sounds
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'shoot.wav'))
player_die_sound = pygame.mixer.Sound(path.join(snd_dir, 'rumble1.wav'))
player2_die_sound = pygame.mixer.Sound(path.join(snd_dir, 'rumble1.wav'))
music_sound = pygame.mixer.Sound(path.join(snd_dir, 'Galaga.mp3'))
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))
explosion_anim = {}
explosion_anim['sm'] = []
explosion_anim['lg'] = []
explosion_anim['player'] =  []

for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)




play_agian = False
game_over = True
mmenu = True
hmenu = False
smenu = False
reset_play1 = False
reset_play2 = False
level_pick = False
oneplayer = False
twoplayer = False
hitdetect = False
reset = False
hscore = 0
# Game loop
running = True
while True:
    if game_over:
        play_again = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        lasers = pygame.sprite.Group()
        player_group = pygame.sprite.Group()
        player2_group = pygame.sprite.Group()
        player = Player()
        player2 = Player2()
        player_group.add(player)
        player2_group.add(player2)
        score = 0
        for i in range(5):
            newmob()
        m = Mob()
    else:
        screen.blit(background, background_rect)
        all_sprites.draw(screen)

    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        level_pick = True
        hmenu = False
        mmenu = False
        smenu = False
    if keys[pygame.K_SPACE]:
        player.shoot()
    if keys[pygame.K_f]:
        player2.shoot()
    if keys[pygame.K_ESCAPE]:
        sys.exit()
    if keys[pygame.K_h]:
        hmenu = True
        mmenu = False
        smenu = False
    if keys[pygame.K_m]:
        mmenu = True
        hmenu = False
        smenu = False
    if keys[pygame.K_s]:
        smenu = True
        hmenu = False
        mmenu = False

    if play_again:
        draw_text(font, screen, "Play Again? Press P.", 25, WIDTH/2, HEIGHT - 400)
        draw_text(font, screen, "No? Press M.", 25, WIDTH/2, HEIGHT - 300)
        if keys[pygame.K_m]:
            mmenu = True
            play_again = False
            hmenu = False
            smenu = False
        if keys[pygame.K_p] and oneplayer:
            reset_play1 = True
        if keys[pygame.K_p] and twoplayer:
            reset_play2 = True
    else:
        all_sprites.update()
        player_group.update()
        player2_group.update()

    if level_pick:
        screen.blit(background, background_rect)
        draw_text(font, screen, "PICK A MODE:", 25, WIDTH/2, HEIGHT - 500)
        draw_text(font, screen, "1 FOR ONE PLAYER", 25, WIDTH/2, HEIGHT - 400)
        draw_text(font, screen, "2 FOR TWO PLAYER", 25, WIDTH/2, HEIGHT - 300)
        if keys[pygame.K_1]:
            oneplayer = True
        if keys[pygame.K_2]:
            twoplayer = True

    if oneplayer:
        hitdetect = True
        game_over = False
        level_pick = False
        twoplayer = False
        player2.hide()
        player_group.draw(screen)
        draw_text(font, screen, str(player.shield), 18, WIDTH / 4, 5)
        draw_text(font, screen, str(score), 18, WIDTH/2, 5)
        draw_shield_bar(screen, 5, 5, player.shield)
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)

    if twoplayer:
        hitdetect = True
        game_over = False
        level_pick = False
        oneplayer = False
        player_group.draw(screen)
        player2_group.draw(screen)
        #draw_shield_bar2(screen, 5, 30, player2.shield)
        draw_shield_bar(screen, 5, 5, player.shield)
        draw_shield_bar2(screen, 5, 30, player2.shield2)
        draw_text(font, screen, str(player.shield), 18, WIDTH / 4, 5)
        draw_text(font, screen, str(player2.shield2), 18, WIDTH / 4, 30)
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
        draw_lives(screen, WIDTH - 100, 30, player2.lives, player2_mini_img)




    if reset_play1:
        hitdetect = True
        all_sprites.update()
        player_group.update()
        player2_group.update()
        screen.blit(background, background_rect)
        player_group.draw(screen)
        all_sprites.draw(screen)
        draw_shield_bar(screen, 5, 5, player.shield)
        draw_text(font, screen, str(player.shield), 18, WIDTH / 4, 5)
        draw_text(font, screen, str(score), 18, WIDTH/2, 5)


    if reset_play2:
        hitdetect = True
        all_sprites.update()
        player_group.update()
        player2_group.update()
        screen.blit(background, background_rect)
        player_group.draw(screen)
        player2_group.draw(screen)
        all_sprites.draw(screen)
        player.lives = 3
        player2.lives = 3
        draw_shield_bar(screen, 5, 5, player.shield)
        draw_shield_bar2(screen, 5, 30, player2.shield2)
        draw_text(font, screen, str(player.shield), 18, WIDTH / 4, 5)
        draw_text(font, screen, str(player2.shield2), 18, WIDTH / 4, 30)
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
        draw_lives(screen, WIDTH - 100, 30, player2.lives, player2_mini_img)



    if mmenu == True:
        screen.blit(background, background_rect)
        draw_text(font, screen, "PYGALA", 64, WIDTH/2, HEIGHT - 500)
        draw_text(font, screen, "Press H for Help", 25, WIDTH/2, HEIGHT - 400)
        draw_text(font, screen, "Press P to Play", 25, WIDTH/2, HEIGHT - 300)
        draw_text(font, screen, "Press S for Top Score", 25, WIDTH/2, HEIGHT - 200)
        pygame.display.flip()

    if hmenu == True:
        screen.blit(background, background_rect)
        draw_text(font, screen, "FOR ONE PLAYER:", 25, WIDTH/2, HEIGHT - 425)
        draw_text(font, screen, "FOR TWO PLAYER:", 25, WIDTH/2, HEIGHT - 250)
        draw_text(font, screen, "Press M to Go Back", 18, WIDTH/2, HEIGHT - 100)
        draw_text(font, screen, "PYGALA", 64, WIDTH/2, HEIGHT - 500)
        draw_text(font, screen, "Use the Arrow Keys to Move", 20, WIDTH/2, HEIGHT - 400)
        draw_text(font, screen, "Use the Space Bar to Shoot", 20, WIDTH/2, HEIGHT - 350)
        draw_text(font, screen, "Use A and D to Move", 20, WIDTH/2, HEIGHT - 200)
        draw_text(font, screen, "Use the F Button to Shoot", 20, WIDTH/2, HEIGHT - 150)



    if smenu == True:
        screen.blit(background, background_rect)
        draw_text(font, screen, "Top Score", 50, WIDTH/2, HEIGHT-400)
        draw_text(font, screen, "PYGALA", 64, WIDTH/2, HEIGHT - 500)
        draw_text(font, screen, str(hscore), 64, WIDTH/2, HEIGHT - 300)



    if score > hscore:
        hscore = score




    # Update
    if hitdetect:
    # check to see if a bullet hit a mob
        hits = pygame.sprite.groupcollide(mobs, lasers , True, True)
        for hit in hits:
            score += 50 - hit.radius
            random.choice(expl_sounds).play()
            newmob()
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)


    # check to see if a mob hit the player

        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        for hit in hits:
            player.shield -= hit.radius * 2
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            newmob()
            if player.shield <= 0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100
                score = 0

        hits = pygame.sprite.spritecollide(player2, mobs, True, pygame.sprite.collide_circle)
        for hit in hits:
            player2.shield2 -= hit.radius * 2
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            newmob()
            if player2.shield2 <= 0:
                player2_die_sound.play()
                death_explosion2 = Explosion(player2.rect.center, 'player')
                all_sprites.add(death_explosion2)
                player2.hide()
                player2.lives -= 1
                player2.shield2 = 100
                score = 0

        if player.lives == 0 and not death_explosion.alive():
            play_again = True
        if player2.lives == 0 and not death_explosion2.alive():
            play_again = True




    # Draw / render
    #screen.fill(WHITE)


    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
