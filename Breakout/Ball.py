import pygame
import Color

class Ball():
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("Ball.png")

        self.__rect = self.image.get_rect()

        self.radius = self.__rect.width//2

        self.__rect.x = 0
        self.__rect.y = 0

        self.dx = 4
        self.dy = -4

    def setPos(self, x, y):
        self.__rect.x = x
        self.__rect.y = y

    def swapXDir(self):
        self.dx = self.dx * -1

    def swapYDir(self):
        self.dy = self.dy * -1

    def getRadius(self):
        return self.radius

    def getLeft(self):
        return self.__rect.left

    def getRight(self):
        return self.__rect.right

    def getTop(self):
        return self.__rect.top

    def getBottom(self):
        return self.__rect.bottom

    def getRect(self):
        return self.__rect

    def move(self):
        self.__rect = self.__rect.move(self.dx, self.dy)

    def draw(self):
        self.screen.blit(self.image, self.__rect)
