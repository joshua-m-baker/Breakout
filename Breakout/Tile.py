import pygame

class Tile():
    def __init__(self, surface, rect, color, health = 1):
        self.surface = surface
        self.rect = rect
        self.color = color
        self.health = health

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def hit(self):
        self.health = self.health - 1

    def update(self):
        if self.health == 0:
            return True
        else:
            return False

