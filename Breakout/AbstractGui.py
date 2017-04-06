import pygame
from pygame.locals import *
import sys
import Color

class AbstractGui(object):
    def __init__(self, image = ""):
        pygame.init()

        #self.backgroundColor = color
        #self.backgroundColor = Color.grey
        try:
            self.image = pygame.image.load(image)

        except pygame.error:
            self.image = pygame.surface.Surface((640, 480))
        
        self.rect = self.image.get_rect()


        self.width = self.rect.width
        self.height = self.rect.height

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.drawBackground()
 
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()

    def drawBackground(self):
        self.screen.blit(self.image, self.rect)

