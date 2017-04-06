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

        #Sprite groups
        self.assets = pygame.sprite.Group() #Everything to be drawn
        self.tiles = pygame.sprite.Group() #All the tiles that can be hit


        #Variables for formatting
        self.tileSpacer = 2
        self.ySpace = 4
        self.yMenuMargin = 40

        #Structure of level
        self.numTiles = 10
        self.numRows = 1

        #Game info
        self.lives = 3
        self.score = 0

        #Boolean to track if they are playing or need to launch the ball
        self.playing = False

        #Add all assets
        self.addAssets()

        self.drawBoard()

        #TODO - text labels/ lives

        #self.textList.append(textLabel(self.screen, "Score: {}".format(self.score), 550, 10, Color.green))
        #self.textList.append(textLabel(self.screen,"Lives: {}".format(self.lives), 5, 10, Color.green))


    def addAssets(self):
        self.addPaddle()
        self.newBall()
        self.makeTiles()
        



    #Make a new ball and place it on the paddle
    def newBall(self):
        
        self.ball = Ball()
        self.assets.add(self.ball)
        x = self.paddle.getWidth()//2 - self.ball.getRadius()
        y = self.paddle.rect.top - 2*self.ball.getRadius()
        self.ball.setPos(x,y)


    #Create the tiles for the round
    def makeTiles(self):
        
        x = self.tileSpacer//2
        y = self.ySpace + self.yMenuMargin

        for i in range(self.numRows):

            for j in range(self.numTiles):
                tile = Tile(x, y)
                self.tiles.add(tile)
                #self.assets.add(tile)
                x += tile.rect.width + self.tileSpacer

            x = self.tileSpacer//2
            y += self.ySpace + tile.rect.height

    def addPaddle(self):
        self.paddle = Paddle(0, self.height - 50)
        self.assets.add(self.paddle)


    def drawBoard(self):
        #Redraw the background to clear off the old stuff
        self.drawBackground()

        #Draw the new assets
        self.assets.draw(self.screen)
        self.tiles.draw(self.screen)

        pygame.display.flip()


    def loop(self):
        #Clock to limit framerate
        clock = pygame.time.Clock()

        #hide the mouse cursor
        pygame.mouse.set_visible(0)
        width = self.screen.get_width()


        keepGoing = True
        while (keepGoing == True):
            clock.tick(60)

            self.assets.update()
            self.drawBoard()

            #TODO - if the tiles are all gone do something 
            if (len(self.tiles) == 0):
                #Win function needed
                keepGoing = False
                sys.exit()


            x = pygame.mouse.get_pos()[0]

            #If the cursor is in the bounds, move the paddle to that location
            #This prevents the paddle from going off the screen
            if ((x >= (self.paddle.getWidth())/2) and (x <= (self.screen.get_width() - self.paddle.getWidth()/2))):
                self.paddle.slide(x-self.paddle.getWidth()/2)

                #If they still need to launch the ball, keep the ball on the middle of the paddle
                if self.playing == False:
                    self.ball.setPos(self.paddle.getMiddle()[0] - self.ball.getRadius()//2, self.ball.getTop())

            #If they are playing:
            if (self.playing == True):
                #Move the ball then check collisions 
                self.ball.move()

                #If it hits a wall, swap the x direction so it bounces
                if ((self.ball.getLeft()) <= 0):
                    self.ball.swapXDir()
                if ((self.ball.getRight()) >= (self.screen.get_width())):
                    self.ball.swapXDir()

                #if it hits the top, score the round, reset the ball and tiles and add another row of them
                if ((self.ball.getTop()) < self.yMenuMargin):
                    #TODO Better scoring mechanism
                    self.score += 1
                    self.playing = False
                    self.ball.kill()
                    self.newBall()
                    self.tiles.empty()
                    
                    if self.numRows <= 6:
                        self.numRows += 1
                    self.makeTiles()
                    time.sleep(.35)

                #If it hits the bottom, they lose a life, reset the ball
                if ((self.ball.getBottom()) > (self.screen.get_height())):
                    self.lives -= 1
                    self.playing = False
                    self.ball.kill()
                    self.newBall()
                    time.sleep(.35)

                #TODO - better collision handling to hit sides of things
                #If the ball hits the paddle, swap the y direction
                #if self.ball.getRect().colliderect(self.paddle.getRect()):
                #    self.ball.swapYDir()
                   

                #If the ball hits the paddle
                if self.ball.getRect().colliderect(self.paddle.getRect()):
                    self.ball.swapYDir()
                    pt = pygame.sprite.collide_mask(self.paddle, self.ball)
                    
                   
                    if (pt != None):
                        pass
                        
                        
                    #If it hits on the left, send it to the left
                    #if it hits the right, send it to the right


                #Check if the ball hit a tile
                for i in self.tiles:
                    if (i.rect.colliderect(self.ball.getRect())):
                        pt = pygame.sprite.collide_mask(i, self.ball)
                        if (pt != None):
                        
                            #if it hits a side edge, swap the x direction
                            #otherwise it hit the top or bottom so swap the y direction
                            if 2 < pt[1] < 18:
                                self.ball.swapXDir()

                            else:
                                self.ball.swapYDir()

                            #i.remove(self.assets, self.tiles)
                            i.kill()
                            #print(self.tiles)
                            #print(self.assets)
                            
                            #i.hit()
                        
                    

            else:
                #If they aren't playing, start the ball if they press space or click
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.playing = True
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.playing = True

            #Check if they quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

g = GameBoard("background3.png")
g.loop()
