import pygame.sprite
from bullet import Bullet
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, xp, yp, sprite):
        super().__init__()
        self.score = 0
        self.speed = speed
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
        self.shoot_cooldown = 0

    def draw(self):
        screen.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)

    # movement function
    def move(self, left, right):
        if left:
            self.rect.x += -self.speed
            self.flip = True
            self.direction_player = -1
        if right:
            self.rect.x += self.speed
            self.flip = False
            self.direction_player = 1

    # shoot function with cooldown
    def shoot_(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 30
            bullet = Bullet(self.rect.centerx + (0.2 * self.rect.size[0]*self.direction_player),
                            self.rect.centery, self.direction_player)
            self.bullet_group.add(bullet)

    # decreases cooldown
    def update(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
