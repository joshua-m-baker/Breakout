import pygame
import Color

class Paddle():
    def __init__(self, screen, x, y):
        
        self.rect = pygame.Rect((x,y), (80, 20))
        self.color = Color.blue
        self.screen = screen

    def slide(self, x):
        self.rect.x = x

    def getRect(self):
        return self.rect

    def getWidth(self):
        return (self.rect.right - self.rect.left)

    def getMiddle(self):
        return self.rect.midtop

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)