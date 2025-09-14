import pygame as pg
import random
from pygame.locals import *
import sys

vec = pg.math.Vector2
WIDTH = 800
HEIGHT = 500
maxvel = 30

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((50,80))
        self.surf.fill((78,205,0))
        self.rect = self.surf.get_rect(center=(100,410))

        self.pos = vec((150,400))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.hasDoubleJump = False
        self.isJumping = False

    def move(self):
        self.acc = vec(0,0.5)
        #self.acc.x += self.vel.x * FRIC
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
        hit = pg.sprite.spritecollide(P1,platform,False)
        if P1.vel.y > 0:
            if hit:
                self.vel.y = 0
                self.pos.y = hit[0].rect.top + 1
                self.isJumping = False

    def jump(self):
        self.isJumping = True
        hit = pg.sprite.spritecollide(P1,platform,False)
        if hit:
            self.vel.y = -12
            self.hasDoubleJump = True
        elif not hit and self.hasDoubleJump:
            self.vel.y = -12
            self.hasDoubleJump = False

    def slide(self):
        if not self.isJumping:
            self.surf = pg.Surface((50,30))
            self.surf.fill((78,205,0))
            self.rect = self.surf.get_rect(center=(100, 460))

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

class Decoration(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface()

P1 = Player()
PT1 = Platform()
platform = pg.sprite.Group()
platform.add(PT1)
sprite_group = pg.sprite.Group()
sprite_group.add(P1)
sprite_group.add(PT1)