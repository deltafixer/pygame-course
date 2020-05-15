import pygame, sys
from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()

# extract dimensions
(windowWidth, windowHeight) = (1024, 768)

background = pygame.image.load('bg.png')
# scale to desired dimensions
background = pygame.transform.scale(background, (windowWidth, windowHeight))

# initialize pygame
pygame.init()

# set window specs
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))

# set window title
pygame.display.set_caption('Neo i virusi')

# player character
playerDimensions = (30, 70)
playerImage = pygame.image.load('neo.png')
playerImage = pygame.transform.scale(playerImage, playerDimensions)
# Rect((left, top), (width, height)) -> Rect
playerRect = playerImage.get_rect()

# set up player rect position
playerRect.topleft = (int(windowWidth / 2) - int(playerDimensions[0] / 2), windowHeight - playerDimensions[1])

# falling object
fallingObjectDimensions = (96, 80)
fallingObjectImage = pygame.image.load('object.png')
fallingObjectImage = pygame.transform.scale(fallingObjectImage, fallingObjectDimensions)
fallingObjectRect = fallingObjectImage.get_rect()

# add background
windowSurface.blit(background, (0, 0))
# add character
windowSurface.blit(playerImage, playerRect)

for i in range(3):
    fallingObjectRect.topleft = (int(windowWidth / 2) + (i - 1) * fallingObjectDimensions[0]  - int(fallingObjectDimensions[0] / 2), int(windowHeight / 2) - fallingObjectDimensions[1])
    windowSurface.blit(fallingObjectImage, fallingObjectRect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                    terminate()
