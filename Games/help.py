import pygame, time
from pygame.locals import *
from MyLibrary import *

class Snake:
    x = []
    y = []
    step = 44
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)
        self.x[1] = 1*44
        self.x[2] = 2*44

    def update(self):
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            for i in range(self.length-1, 0, -1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def move_right(self):
        self.direction = 0

    def move_left(self):
        self.direction = 1

    def move_up(self):
        self.direction = 2

    def move_down(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))


class Game:
    def is_collistion(self, x1, y1, x2, y2, bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False

class App:
    width = 800
    height = 800
    player = 0



    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = Snake(3)
        self.game = Game()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
        pygame.display.set_caption('Hello There')
        self._running = True
        self._image_surf = pygame.image.load("Square.jpg")

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()

        for i in range(2, self.player.length):
            if self.game.is_collistion(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 40):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                exit(0)
        pass

    def on_render(self):
        self._display_surf.fill((255,255,255))
        self.player.draw(self._display_surf, self._image_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False


        while ( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_d]:
                self.player.move_right()

            if keys[K_RIGHT]:
                self.player.move_right()

            if keys[K_a]:
                self.player.move_left()

            if keys[K_LEFT]:
                self.player.move_left()

            if keys[K_w]:
                self.player.move_up()

            if keys[K_UP]:
                self.player.move_up()

            if keys[K_s]:
                self.player.move_down()

            if keys[K_DOWN]:
                self.player.move_down()

            self.on_loop()
            self.on_render()

            time.sleep(50.0 / 1000.0)
        self.on_cleanup()

if __name__ == "__main__" :
    app = App()
    app.on_execute()
