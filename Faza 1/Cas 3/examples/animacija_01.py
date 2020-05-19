import pygame as pg
import pygamebg
import random

#inicijalizacija prozora
(sirina, visina) = (400, 400)
pg.init()
prozor = pg.display.set_mode((sirina, visina))
prozor.fill(pg.Color("white"))

#odredjivanje broja kvadrata po kolonama i njihova velicina
broj_kvadrata = 10
a = int(sirina / broj_kvadrata)

#funkcija koja će u dati neku nasumičnu boju u RGB obliku 
def nasumicna_boja():
    return(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#funkcija koja iscrtava mrežu kvadrata nasumičnih boja 
def crtaj():
    for i in range(broj_kvadrata):
        for j in range(broj_kvadrata):
            pg.draw.rect(prozor, nasumicna_boja(), (j*a, i*a, a, a))

#funkciju crtaj ćemo pozivati svake sekunde pa će se tako menjati boja kvadrata
pygamebg.frame_loop(1, crtaj)
