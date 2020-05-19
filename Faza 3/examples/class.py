import pygame, sys, random
from pygame.locals import *

# izolovanje dimenzija
(windowWidth, windowHeight) = (1024, 768)

textColor = (139, 0, 0)

background = pygame.image.load('bg.png')
# skaliranje na željenu dimenziju
background = pygame.transform.scale(background, (windowWidth, windowHeight))

playerMoveRate = 5

def terminate():
    pygame.quit()
    sys.exit()

def collided(playerRect, fallingObjects):
    for fallingObject in fallingObjects:
        if playerRect.colliderect(fallingObject['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textObject = font.render(text, 1, textColor)
    textRect = textObject.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObject, textRect)

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

# inicijalizacija pygame-a
pygame.init()

# podešavanja prozora
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))

# postavljanje naslova prozora
pygame.display.set_caption('Neo i virusi')
pygame.mouse.set_visible(False)

# font
font = pygame.font.SysFont(None, 48)

# melodije
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

# uvodna poruka
drawText('Koristi miša ili strelice kako bi izbegavao viruse.', font, windowSurface, int(windowWidth / 2) - 300, int(windowHeight / 2) - 50)
drawText('Pritisni bilo koji taster za početak.', font, windowSurface, int(windowWidth / 2) - 300, int(windowHeight / 2))
pygame.display.update()
waitForPlayerToPressKey()

# slika junaka
playerImage = pygame.image.load('neo.png')
playerDimensions = (30, 70)
playerImage = pygame.transform.scale(playerImage, playerDimensions)
playerRect = playerImage.get_rect()

# podešavanje pozicije pravougaonika koji okružuje junaka
playerRect.topleft = (int(windowWidth / 2) - int(playerDimensions[0] / 2), windowHeight - playerDimensions[1])

# padajući objekti (virusi)
fallingObjectImage = pygame.image.load('object.png')
fallingObjectDimensions = (96, 80)
fallingObjectImage = pygame.transform.scale(fallingObjectImage, fallingObjectDimensions)
fallingObjectRect = fallingObjectImage.get_rect()

pygame.display.update()

# konstante
fallingObjectMinSize = 10
fallingObjectMaxSize = 50
fallingObjectMinSpeed = 1
fallingObjectMaxSpeed = 8
fallingObjectCreationRate = 6
framesPerSecond = 100

mainClock = pygame.time.Clock()

topScore = 0

while True:
    playerRect.topleft = (int(windowWidth / 2), int(windowHeight - 50))
    moveLeft = moveRight = moveUp = moveDown = False
    fallingObjects = []
    fallingObjectCounter = 0
    score = 0
    pygame.mixer.music.play(-1, 0.0)
    reverseCheat = slowCheat = False

    while True:
        score += 1

        for event in pygame.event.get():
            # pritisnuto dugme na tastaturi
            if event.type == KEYDOWN:
                # leva strelica ili dugme A
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = True

                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = True

                if event.key == K_UP or event.key == ord('w'):
                    moveUp = True

                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = True

                if event.key == ord('q'):
                    reverseCheat = True

                if event.key == ord('e'):
                    slowCheat = True

            # otpušteno dugme sa tastature
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False

                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False

                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False

                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

                if event.key == ord('q'):
                    reverseCheat = False
                    score = 0
                    
                if event.key == ord('e'):
                    slowCheat = False
                    score = 0

            # pomeraj miša
            if event.type == MOUSEMOTION:
                playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)

            # klik na X dugme prozora
            if event.type == QUIT:
                terminate()

        # dodavanje novog virusa na početak prozora (samo ukoliko nije aktivan nijedan cheat!!!)
        if not reverseCheat and not slowCheat:
            fallingObjectCounter +=1
        if fallingObjectCounter == fallingObjectCreationRate:
            fallingObjectCounter = 0
            fallingObjectRandomSize = random.randint(fallingObjectMinSize, fallingObjectMaxSize)
            newFallingObject = {
                        'rect': pygame.Rect(random.randint(0, windowWidth - fallingObjectRandomSize), 0 - fallingObjectRandomSize, fallingObjectRandomSize, fallingObjectRandomSize), 
                        'speed': random.randint(fallingObjectMinSpeed, fallingObjectMaxSpeed),
                        'surface':pygame.transform.scale(fallingObjectImage, (fallingObjectRandomSize, fallingObjectRandomSize)),
                        }

            fallingObjects.append(newFallingObject)

        # pomeranje junaka
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * playerMoveRate, 0)
        if moveRight and playerRect.right < windowWidth:
            playerRect.move_ip(playerMoveRate, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * playerMoveRate)
        if moveDown and playerRect.bottom < windowHeight:
            playerRect.move_ip(0, playerMoveRate)

        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

        # dodavanje pozadine
        windowSurface.blit(background, (0, 0))

        # dodavanje junaka
        windowSurface.blit(playerImage, playerRect)

        # dodavanje padajućih objekata (virusa)
        for fallingObject in fallingObjects:
            windowSurface.blit(fallingObject['surface'], fallingObject['rect'])

        # kretanje padajućih objekata (virusa)
        for fallingObject in fallingObjects:
            if not reverseCheat and not slowCheat:
                fallingObject['rect'].move_ip(0, fallingObject['speed'])
            elif reverseCheat:
                fallingObject['rect'].move_ip(0, -5)
            elif slowCheat:
                fallingObject['rect'].move_ip(0, 1)

        # brisanje padajućih objekata (virusa)
        for fallingObject in fallingObjects[:]:
            if fallingObject['rect'].top > windowHeight:
                fallingObjects.remove(fallingObject)

        # crtanje razultata
        drawText('Rekord: %s' % (topScore), font, windowSurface, 10, 40)
        drawText('Rezultat: %s' % (score), font, windowSurface, 10, 0)

        # kraj igre
        if collided(playerRect, fallingObjects):
            if score > topScore:
                topScore = score 
            break

        pygame.display.update()
        mainClock.tick(framesPerSecond)

    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('Kraj igre!', font, windowSurface, int(windowWidth / 2) - 100, int(windowHeight / 2) - 50)
    drawText('Pritisni bilo koji taster za novu igru.', font, windowSurface, int(windowWidth / 2) - 300, int(windowHeight / 2))
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()
