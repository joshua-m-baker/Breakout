import pygame
import Color

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #self.rect = pygame.Rect((x,y), (80, 20))
        self.image = pygame.image.load("Paddle.png")
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.color = Color.blue
        #self.screen = screen


    def slide(self, x):
        self.rect.x = x

    def getRect(self):
        return self.rect

    def getWidth(self):
        return (self.rect.right - self.rect.left)

    def getMiddle(self):
        return self.rect.midtop

    #def draw(self):
        #pygame.draw.rect(self.screen, self.color, self.rect)