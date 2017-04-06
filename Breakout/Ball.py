import pygame
import Color

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.screen = screen
        self.image = pygame.image.load("ball1.png")
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = pygame.Rect((0,0),(20, 20))

        self.radius = self.rect.width//2

        self.rect.x = 0
        self.rect.y = 0

        self.dx = 4
        self.dy = -4

    def setPos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def swapXDir(self):
        self.dx = self.dx * -1

    def swapYDir(self):
        self.dy = self.dy * -1

    def getRadius(self):
        return self.radius

    def getLeft(self):
        return self.rect.left

    def getRight(self):
        return self.rect.right

    def getTop(self):
        return self.rect.top

    def getBottom(self):
        return self.rect.bottom

    def getRect(self):
        return self.rect

    def move(self):
        self.rect = self.rect.move(self.dx, self.dy)

    #def draw(self):
        #pygame.draw.circle(self.screen, Color.red, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)
        #self.screen.blit(self.image, self.rect)
