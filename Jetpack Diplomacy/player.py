import pygame.sprite
from bullet import Bullet
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, xp, yp, sprite):
        super().__init__()
        self.score = 0
        self.vel_y = 0
        self.speed = speed
        self.xp = xp
        self.yp = yp
        self.sprite = sprite
        self.bullet_list = []
        self.bullet_group = pygame.sprite.Group()
        self.direction_player = 1
        self.flip = False
        self.image = pygame.transform.scale(self.sprite, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (xp, yp)
        self.shoot = False
        self.hit = False
        self.stop = False
        self.alive = True
        self.shoot_cooldown = 0

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    # movement function
    def move(self, left, right, jump):
        dy = 0
        if left:
            self.rect.x += -self.speed
            self.flip = True
            self.direction_player = -1
        if right:
            self.rect.x += self.speed
            self.flip = False
            self.direction_player = 1
        if jump:
            self.vel_y = -4
        self.vel_y += gravity
        dy += self.vel_y
        self.rect.y += dy

        # ensure player stays on screen
        if self.rect.left + self.speed < 0:
            self.rect.x += -self.rect.left
        if self.rect.right + self.speed > screen_width:
            self.rect.x += screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 20:
            self.vel_y = 0
            dy = screen_height - 20 - self.rect.bottom
        self.rect.y += dy

    # shoot function with cooldown
    def shoot_(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 30
            bullet = Bullet(self.rect.centerx + (0.2 * self.rect.size[0]*self.direction_player),
                            self.rect.centery, self.direction_player)
            self.bullet_group.add(bullet)
            self.bullet_list.append(bullet)

    # decreases cooldown
    def update(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def reposition(self):
        self.stop = False
        self.hit = False
        self.xp = xp1
        self.yp = yp1
