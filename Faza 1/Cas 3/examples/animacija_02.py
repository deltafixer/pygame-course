import pygame, sys
from pygame.locals import *

#inicijalizujmo prozor
pygame.init()
(sirina, visina) = (600, 500)
ekran = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption("Setajući kvadrat")
zuta = 255,255,0

#definisimo kvadrat i njegove pozicije
stranica_kvadrata = 100
debljina_linije = 0 #popunjeno skroz
x_pozicija = 300
y_pozicija = 250
x_brzina = 0.5
y_brzina = 0.5

while True: #ovaj deo koda će se non-stop izvršavati i tako simuliramo animaciju
    for dogadjaj in pygame.event.get():
        if dogadjaj.type in (QUIT, KEYDOWN):
            sys.exit()
    ekran.fill((0,0,200))
    
    #pomeramo kvadrat
    x_pozicija += x_brzina
    y_pozicija += y_brzina

    #zadrzavamo kvadrat unutar prozora
    if x_pozicija > sirina - stranica_kvadrata or x_pozicija < 0:
        x_brzina = -x_brzina
    if y_pozicija > visina - stranica_kvadrata or y_pozicija < 0:
        y_brzina = -y_brzina

    #crta kvadrat
    pos = x_pozicija, y_pozicija, stranica_kvadrata, stranica_kvadrata
    pygame.draw.rect(ekran, zuta, pos, debljina_linije)
    pygame.display.update()
