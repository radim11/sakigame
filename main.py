import pygame as pg
import sys
import objects
import random
from pygame.locals import *

pg.init()
pg.display.set_caption("Saki Runner")
screen = pg.display.set_mode((objects.WIDTH,objects.HEIGHT))
background = pg.Surface(screen.get_size())
background.fill((60, 10, 10))
FramePerSec = pg.time.Clock()
FPS = 30
while True:
    pressedKey = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_UP:
            objects.P1.jump()
            objects.P1.idle()
        if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            objects.P1.slide()
        if event.type == pg.KEYUP and event.key == pg.K_DOWN:
            objects.P1.idle()
    screen.blit(background, (0, 0))

    objects.P1.move()
    objects.P1.update()

    for entity in objects.sprite_group:
        screen.blit(entity.surf,entity.rect)

    pg.display.update()
    FramePerSec.tick(FPS)
