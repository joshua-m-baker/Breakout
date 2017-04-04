import pygame
from pygame.locals import *
import sys
import Color

class AbstractGui(object):
    def __init__(self, color):
        pygame.init()

        self.backgroundColor = color

        self.width = 640
        self.height = 480

        pygame.font.init()
        self.font = pygame.font.Font(None, 30)

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.backgroundColor)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()

    def drawText(self, text, x, y, color ):

        textSize = self.font.size(text)

        textWidth = textSize[0]
        textHeight = textSize[1]

        rect = pygame.Rect(((x, y), (textWidth, textHeight)))

        rectX = rect.left
        rectY = rect.top

        rectWidth = rect.width
        rectHeight = rect.height

        textX = rectX + rectWidth//2 - textWidth//2
        textY = rectY + rectHeight//2 - textHeight//2

        textRender = self.font.render(text, True, color)
        #pygame.draw.rect(self.screen, self.black, pygame.Rect((rectX-1, rectY - 1), (rectWidth + 2, rectHeight + 2)))
        #pygame.draw.rect(self.screen, self.blue, rect)
        self.screen.blit(textRender, (textX, textY))

        #pygame.display.flip()