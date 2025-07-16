import pygame as pg
import random
from pygame.locals import *
import sys

vec = pg.math.Vector2
FRIC = -0.12
WIDTH = 800
HEIGHT = 500
maxvel = 20

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((50,80))
        self.surf.fill((78,205,0))
        self.rect = self.surf.get_rect(center=(100,410))

        self.pos = vec((150,400))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,0.5)
        self.acc.x += self.vel.x * FRIC
        if self.vel.y > maxvel:
            self.acc.y = 0
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def idle(self):
        self.surf = pg.Surface((50,80))
        self.surf.fill((78,205,0))
        self.rect = self.surf.get_rect(center=(100, 410))

    def update(self):
        hit = pg.sprite.spritecollide(P1,platforms,False)
        if P1.vel.y > 0:
            if hit:
                self.vel.y = 0
                self.pos.y = hit[0].rect.top + 1

    def jump(self):
        #jump = True
        hit = pg.sprite.spritecollide(P1,platforms,False)
        if hit: #or jump
            self.vel.y = -12

    def duck(self):
        self.surf = pg.Surface((50,30))
        self.surf.fill((78,205,0))
        self.rect = self.surf.get_rect(center=(100, 460))
        hit = pg.sprite.spritecollide(P1,platforms,False)
        if not hit:
            self.vel.y = maxvel

class Platform(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((WIDTH,60))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center=((WIDTH)/2,(HEIGHT)-30))

class Obstacle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface()

P1 = Player()
PT1 = Platform()
platforms = pg.sprite.Group()
platforms.add(PT1)
sprite_group = pg.sprite.Group()
sprite_group.add(P1)
sprite_group.add(PT1)