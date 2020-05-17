import pygame, sys
from pygame.locals import *

backgroundColor = (255, 255, 255)

# extract dimensions
(windowWidth, windowHeight) = (800, 600)

background = pygame.image.load('bg.png')
# scale to desired dimensions
background = pygame.transform.scale(background, (windowWidth, windowHeight))

#constants
playerMoveRate = 5

def terminate():
    pygame.quit()
    sys.exit()

# initialize pygame
pygame.init()

# set window specs
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))

# set window title
pygame.display.set_caption('Neo i virusi')
pygame.mouse.set_visible(False)

# player character
playerImage = pygame.image.load('neo.png')
playerDimensions = (30, 70)
playerImage = pygame.transform.scale(playerImage, playerDimensions)
# Rect((left, top), (width, height)) -> Rect
playerRect = playerImage.get_rect()

# set up player rect position
playerRect.topleft = (int(windowWidth / 2) - int(playerDimensions[0] / 2), windowHeight - playerDimensions[1])

# falling object
fallingObjectImage = pygame.image.load('object.png')
fallingObjectDimensions = (96, 80)
fallingObjectImage = pygame.transform.scale(fallingObjectImage, fallingObjectDimensions)
fallingObjectRect = fallingObjectImage.get_rect()

#pygame.display.update()

playerRect.topleft = (int(windowWidth / 2), int(windowHeight - 50))
    

while True:
    moveLeft = moveRight = moveUp = moveDown = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                # pritisnut 'a' taster na tastaturi 
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = True

                # pritisnut 'd' taster na tastaturi 
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = True

                # pritisnut 'w' taster na tastaturi 
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = True

                # pritisnut 's' taster na tastaturi 
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()

                # otpušten 'a' taster na tastaturi
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False

                # otpušten 'd' taster na tastaturi
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                    
                # otpušten 'w' taster na tastaturi
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False

                # otpušten 's' taster na tastaturi
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

            if event.type == MOUSEMOTION:
                playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)


        # pomeraj igrača
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * playerMoveRate, 0)
        if moveRight and playerRect.right < windowWidth:
            playerRect.move_ip(playerMoveRate, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * playerMoveRate)
        if moveDown and playerRect.bottom < windowHeight:
            playerRect.move_ip(0, playerMoveRate)

        # zadržati pokazivač miša unutar prozora
        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

        # dodati pozadinu
        windowSurface.blit(background, (0, 0))
        
        for i in range(3):
            fallingObjectRect.topleft = (int(windowWidth / 2) + (i - 1) * fallingObjectDimensions[0]  - int(fallingObjectDimensions[0] / 2), int(windowHeight / 2) - fallingObjectDimensions[1])
            windowSurface.blit(fallingObjectImage, fallingObjectRect)

        # dodati igrača
        windowSurface.blit(playerImage, playerRect)

        pygame.display.update()

