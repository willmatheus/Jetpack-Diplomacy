import pygame.sprite

from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, xp, yp, sprite):
        super().__init__()
        self.xp = xp
        self.yp = yp
        self.sprite = sprite
        self.direction = 1
        self.flip = False
        self.bullet_Sprites = pygame.sprite.Group()
        self.img = pygame.transform.scale(self.sprite, (200, 200))
        self.rect = self.img.get_rect()
        self.rect.center = (xp, yp)

    def draw(self):
        screen.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.rect.x += -speed
            self.flip = True
            self.direction = -1
        if key[pygame.K_d]:
            self.rect.x += speed
            self.flip = False
            self.direction = 1
