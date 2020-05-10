import pygame as pg
import pygamebg
import random

(width, height) = (1024, 768)
window = pygamebg.open_window(width, height, "Slovo E")

window.fill([255, 255, 255])

pg.draw.line(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (300, 150), (300, 550), 3)

for i in range(3):
    pg.draw.line(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (300, 150 + i * 200), (500, 150 + i * 200), 3)

pygamebg.wait_loop()
