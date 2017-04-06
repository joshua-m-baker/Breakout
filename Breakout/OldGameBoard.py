from AbstractGui import AbstractGui
from Tile import Tile
from Ball import Ball
from Paddle import Paddle
from textLabel import textLabel
import Color
import pygame
import sys
import math
import time

class GameBoard(AbstractGui):
    def __init__(self, image):
        super().__init__(image)

        self.assets = pygame.sprite.Group()
        self.paddle = Paddle(self.screen, 0, self.height-50)
        self.assets.add(self.paddle)
        
        self.tileSpacer = 2
        self.ySpace = 4
        self.yMenuMargin = 40
        self.numTiles = 10
        self.numRows = 6

        self.lives = 3
        self.score = 0

        #self.tileList = []
        self.tiles = pygame.sprite.Group()
        self.textList = []

        

        self.playing = False

        self.addTiles(self.numRows)
        self.newBall()

    def addTiles(self, numRows):
        #tileWidth = ((self.screen.get_width() - self.tileSpacer)//(self.numTiles))
        tileWidth = 62
        tileHeight = 20
        x = self.tileSpacer//2
        y = self.ySpace + self.yMenuMargin

        self.textList.append(textLabel(self.screen, "Score: {}".format(self.score), 550, 10, Color.green))
        self.textList.append(textLabel(self.screen,"Lives: {}".format(self.lives), 5, 10, Color.green))

        for i in range(numRows):

            
            color = Color.randomColor()

            for j in range(self.numTiles):
                #tileRect = pygame.Rect((x,y), (tileWidth, tileHeight))
                #self.tileList.append(Tile(self.screen, tileRect, color))
                self.tiles.add(Tile(x, y, color))
                x += tileWidth + self.tileSpacer

            x = self.tileSpacer//2
            y += self.ySpace + tileHeight

    def newBall(self):
        self.ball = Ball(self.screen)
        self.assets.add(self.ball)
        x = self.paddle.getWidth()//2 - self.ball.getRadius()
        y = self.paddle.rect.top - 2*self.ball.getRadius()
        self.ball.setPos(x,y)

    def clear(self):
        pass
        #self.screen.blit(self.screen, self.ball.getRect(), )
        #pygame.display.flip()

    def drawBoard(self):
        #self.screen.fill(self.backgroundColor)
        self.screen.blit(self.image, self.rect)
        self.tiles.draw(self.screen)
        #for i in self.tileList:
        #    i.draw()
        for i in self.textList:
            i.draw()
        #self.ball.draw()
        self.assets.draw(self.screen)
        pygame.display.flip()

    def mainLoop(self):
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(0)
        width = self.screen.get_width()
        keepGoing = True
        while (keepGoing == True):
            clock.tick(60)

            if (len(self.tiles) == 0):
                #Win function needed
                keepGoing = False
                sys.exit()

            x = pygame.mouse.get_pos()[0]

            #if (x >= (width-self.paddle.getWidth()/2)):
            #    pygame.mouse.set_pos((width-self.paddle.getWidth()/2), self.height-50)

            if ((x >= (self.paddle.getWidth())/2) and (x <= (self.screen.get_width() - self.paddle.getWidth()/2))):
                self.paddle.slide(x-self.paddle.getWidth()/2)
                if self.playing == False:
                    self.ball.setPos(self.paddle.getMiddle()[0] - self.ball.getRadius()//2, self.ball.getTop())

            if (self.playing == True):
                self.ball.move()

                if ((self.ball.getLeft()) < 0):
                    self.ball.swapXDir()
                if ((self.ball.getRight()) > (self.screen.get_width())):
                    self.ball.swapXDir()

                if ((self.ball.getTop()) < self.yMenuMargin):
                    self.score += 1
                    self.playing = False
                    self.newBall()
                    self.tileList.empty()
                    if self.numRows <= 6:
                        self.numRows += 1
                    self.addTiles(self.numRows)
                    time.sleep(.5)
                    #self.ball.swapYDir()

                if ((self.ball.getBottom()) > (self.screen.get_height())):
                    self.lives -= 1
                    self.playing = False
                    self.newBall()
                    time.sleep(.5)

                if self.ball.getRect().colliderect(self.paddle.getRect()):
                    self.ball.swapYDir()

                #for i in self.tileList:
                for i in self.tiles:
                    rect = self.ball.getRect()
                    if rect.colliderect(i.rect):
                        self.ball.swapYDir()
                        i.hit()
                        if (i.update() == True):
                            self.tileList.remove(i)

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.playing = True
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.playing = True
                      
                    
            self.drawBoard()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    #pygame.QUIT()

