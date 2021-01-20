import pygame
import math
import random
pygame.init()
screenHeight = 720
screenWidth = 1080
screen = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption("<--- Python")
clock = pygame.time.Clock()

#pitfall
#galaga
#circle memory game
#some sort of phase based survival game with blockies

rowNum = 12
colNum = 8
map = []
for row in range(rowNum):
    map.append([])
    for col in range(colNum):
        map[row].append(0)


def Main(): 
    # Loop until the user clicks the close button.
    frameCount = 0
    done = False
    #pygame.mouse.set_pos([0,0])

    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass


        screen.fill((0,0,0))

        for x in range(rowNum):
            for y in range(colNum):
                pygame.Surface.fill(screen, (0,0,0), [(screenWidth / rowNum) * x, (screenHeight / colNum) * y, (screenWidth / rowNum) - 2, (screenHeight / colNum) - 2], 1)
        
 


        frameCount += 1
        pygame.display.flip()
        clock.tick(30)

class Map:
    def __init__(self):
        
        
        
class Player:
    def __init__(self):
        pass

Main()






















#make a game where player trace out a path beforehand and try to cut the other players line in order to win


























