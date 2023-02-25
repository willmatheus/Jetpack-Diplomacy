import pygame.sprite
from bullet import Bullet
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, xp, yp, sprite):
        super().__init__()
        self.score = 0
        self.xp = xp
        self.yp = yp
        self.sprite = sprite
        self.bullet_list = []
        self.bullet_group = pygame.sprite.Group()
        self.direction_player = 1
        self.flip = False
        self.img = pygame.transform.scale(self.sprite, (200, 200))
        self.rect = self.img.get_rect()
        self.rect.center = (xp, yp)
        self.shoot = False
        self.alive = True
        self.shoot_time = 0

    def draw(self):
        screen.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)

    # movement function
    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.rect.x += -speed
            self.flip = True
            self.direction_player = -1
        if key[pygame.K_d]:
            self.rect.x += speed
            self.flip = False
            self.direction_player = 1
    # shoot function
    def shoot_(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.shoot = True
    # update bullets
    def update(self):
        if self.shoot:
            bullet = Bullet(self.rect.centerx + (self.rect.size[0]), self.rect.centery, self.direction_player)
            self.bullet_group.add(bullet)
