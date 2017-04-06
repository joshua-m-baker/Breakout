import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("tile2.png")
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 1

    #def draw(self):
        #pygame.draw.rect(self.surface, self.color, self.rect)  

    def hit(self):
        self.health = self.health - 1
        

    def update(self):
        if self.health <= 0:
            self.kill()
           

