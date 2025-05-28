# -*- coding: utf-8 -*-
"""
Created on Thu May 15 01:17:09 2025

@author: oogbo
"""

import pygame
from pygame.locals import *
from pygame import *

pygame.init()

clock = pygame.time.Clock()
fps = 60


screen_width, screen_height = 700, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer Game")


sunImage = pygame.image.load("sun.png",)
bgImage = pygame.image.load("bg.png")

noOfTiles = 20
tileSizeH = screen_height/noOfTiles #tile size for vertical lines, necesaasry for when screen width nd screen height are different
tileSizeV = screen_width/noOfTiles


def drawGrid(): #draws gridline to help partition my screen. Not necesarry but helpful to visualize how to place things
    for line in range(noOfTiles):
         draw.line(screen, (255,255,255), ( 0, (line+1)*tileSizeH ) , ( screen_width, (line+1)*tileSizeH )) #horizontal line
         draw.line(screen,  (255,255,255), ( (line+1)*tileSizeV , 0),  ( (line+1)*tileSizeV ,screen_height) )


world_layout =  [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class World():
    def __init__(self, layout):
        
        self.tileList =[]
        
        dirtImage = pygame.image.load("dirt.png")
        grassImage = pygame.image.load("grass.png")
         
        #Standard use of a nested for loop to display things in a grid()
        row_no = 0
        for row in layout: 
            col_no = 0
            for tile in row:
                if tile == 1:
                    img= pygame.transform.scale(dirtImage, (tileSizeV,tileSizeH)) #resizes the image to fit the necessary dimensions for our grid. tileSizeV represents the image width and tileSizeH represents the image height; 
                    imgRect = img.get_rect() #creates rectangle object to store our cordinates so we can decide where to put the image / where to find the image in future. by default the rectangle will start at (0,0) and have the same size as the image
                    imgRect.x= col_no * tileSizeV #rect x is the x coordinate where our image will be placed (x,...)
                    imgRect.y= row_no *tileSizeH  #rect y is the y coordinate where our image will be placed  (...,y) as a result our image is placed at (x,y)
                    tile = (img,imgRect) #we store the image and its coordinates in a tuple
                    self.tileList.append(tile) #we append this tuple to a list so we can easily connect each image to its respective coordinate
                if tile == 2:
                    img = pygame.transform.scale(grassImage, (tileSizeV, tileSizeH))
                    imgRect = img.get_rect()
                    imgRect.x = col_no * tileSizeV
                    imgRect.y = row_no * tileSizeH
                    tile = (img, imgRect)
                    self.tileList.append(tile)
                col_no +=1 #column value is updated within each row for each tile(column within the row)
            row_no +=1 #row value is only updated at the end of each row iteration
            
            
    def draw(self):
         for tile in self.tileList:
             screen.blit(tile[0], tile[1]) #the tile list is used to place its image in the correct coordinate on the screen
             

class Player():
    def __init__(self, x, y):
        player1 = image.load("guy1.png")
        self.image = transform.scale(player1, (35,70))
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
        self.jumped = False
        self.vel_y =0 
        '''value of initial velocity assiged as an instant variable rather than a variable for the update method so that it is:
                       1)Independent of any changes that occur to dy based on up/down key presses 
                       2)Set once(only -7 once space is pressed and released), doesnt reset to 0 everytime like dy and dx variables instead it remembers its last value and we apply gravity to it to slow it down on each frame, thereby bringing the image back down
                       We can not use dy becasy dy is reset to 0 each frame(it has to otherwise it wont work for up/down key presses)
                      '''
        self.gravity = +0.5
    def update(self):
        
        dy =0
        dx=0
        #get key presses
        key = pygame.key.get_pressed() #returns a list of true/false for all keys. pressed keys are marked true, unpressed keys are false. you can find a keys true/false value using its contasnt(eg K_SPACE) as the index
        
        #This is the meachnism we will use to move the player while preventing collision:
        #calculate new player position based on dx or dy 
        #check for collision 
        #update player coordinates
        
        if key[pygame.K_RIGHT]:
            dx = +2
            
        if key[pygame.K_LEFT]:
            dx = -2
            
        if key[pygame.K_DOWN]:
            dy = +2
        
        if key[pygame.K_SPACE] and not self.jumped: #player only jumps when space bar is pressed and jumped is false
            self.vel_y = -7
            self.jumped =True
         
        if not key[pygame.K_SPACE]: #jumped is only false when keyboard space bar was previosly released    
            self.jumped = False
        
            
        '''if key[pygame.K_SPACE]:
            
            keyUpEvents = pygame.event.get(pygame.KEYUP)
            for event in keyUpEvents:
                if keyUpEvents.lenth()>0 and event.key == K_SPACE:
                    self.vel_y = -7 '''
                    
         #note to self: learn how to debud when they function requires user/keyboard input   
        
        dy += self.vel_y   #keep updating y position based on current speed and direction      
        if self.vel_y < +7:
            self.vel_y += self.gravity    #keep reducing velocity using gravity
            
        #update player coordinates
        self.rect.x += dx  
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy=0
            
        #draw player on screen    
        screen.blit(self.image, self.rect)           
            
'''
if key[pygame.K_RIGHT]:
    dx = (+2,)
    
if key[pygame.K_LEFT]:
    dx = (-2,)
    
if key[pygame.K_UP]:
    dy = (-2,)    
    
if key[pygame.K_DOWN]:
    dy = (+2,)
    
if key[pygame.K_SPACE]:
    dy =(-10,-10,-10,-10,-10,-10,-10,+10,+10,+10,+10,+10,+10,+10)

    
for move in dx:
    self.rect.x += move #adjusting player coordinates
    screen.blit(self.image, self.rect)
for move in dy:
    self.rect.y += move
    screen.blit(self.image, self.rect)
'''
        
                   
        
world = World(world_layout)         
player = Player(70, screen_height-105) #based on 700px height/20, 1 tile is 35px tall. player is 70px tall so all together the top left of players corrdinates should be 105(35+70)px from the bottom of the screen. height is counted in a downward direction not upward 


running = True

while running:
    
        clock.tick(fps) #adds frame rate
        
        pygame.display.update() #important otherwise your screen will not be updates and your wont see your images
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.blit(bgImage, [0,0])         #this function is what actually place the image on the screen  
        screen.blit(sunImage, [50,50])      #The order in which you place images matter, if you place the sunImage before the bgImage then you will not be able to see the sunImage
        world.draw()
        player.update()
        drawGrid()

       
 
pygame.quit()


