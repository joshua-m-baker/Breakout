import pygame

class textLabel():
    def __init__(self, screen, text, x, y, color):

        self.screen = screen

        self.x = x
        self.y = y

        pygame.font.init()
        self.font = pygame.font.Font(None, 30)

        self.text = text
        self.color = color

        self.textWidth = self.font.size(text)[0]
        self.textHeight = self.font.size(text)[1]


    def updateText(self, text):
        self.text = text

    def draw(self):
        textRender = self.font.render(self.text, True, self.color)
        self.screen.blit(textRender, (self.x, self.y))