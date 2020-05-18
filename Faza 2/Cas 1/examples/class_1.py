import pygame, sys
from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()

# izolovanje dimenzija
(windowWidth, windowHeight) = (1024, 768)

background = pygame.image.load('bg.png')
# skaliranje na željenu dimenziju
background = pygame.transform.scale(background, (windowWidth, windowHeight))

# inicijalizacija pygame-a
pygame.init()

# set window specs
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))

# postavljanje naslova prozora
pygame.display.set_caption('Neo i virusi')

# slika junaka
playerDimensions = (30, 70)
playerImage = pygame.image.load('neo.png')
playerImage = pygame.transform.scale(playerImage, playerDimensions)
playerRect = playerImage.get_rect()

# podešavanje pozicije pravougaonika koji okružuje junaka
playerRect.topleft = (int(windowWidth / 2) - int(playerDimensions[0] / 2), windowHeight - playerDimensions[1])

# padajući objekti (virusi)
fallingObjectDimensions = (96, 80)
fallingObjectImage = pygame.image.load('object.png')
fallingObjectImage = pygame.transform.scale(fallingObjectImage, fallingObjectDimensions)
fallingObjectRect = fallingObjectImage.get_rect()

# dodavanje pozadine
windowSurface.blit(background, (0, 0))
# dodavanje junaka
windowSurface.blit(playerImage, playerRect)

for i in range(3):
    fallingObjectRect.topleft = (int(windowWidth / 2) + (i - 1) * fallingObjectDimensions[0]  - int(fallingObjectDimensions[0] / 2), int(windowHeight / 2) - fallingObjectDimensions[1])
    windowSurface.blit(fallingObjectImage, fallingObjectRect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        # klik na X dugme prozora
        if event.type == QUIT:
            terminate()

        # otpuštanje ESC dugmeta na tastaturi (događaj nakon što kliknemo)
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                    terminate()
