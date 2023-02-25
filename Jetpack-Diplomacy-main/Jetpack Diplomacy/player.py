from config import *
import math
from bullet import Bullet


class Player:
    def __init__(self, sprite, xp, yp, ang):
        self.xp = xp
        self.yp = yp
        self.ang = ang
        self.sprite = sprite
        self.sprite = pygame.transform.scale(self.sprite, (200, 170))
        self.sprite = pygame.transform.rotate(self.sprite, self.ang)
        self.bullets = []  # list of bullets shot by this player
        self.bullet_speed = 5  # set bullet speed
        screen.blit(self.sprite, (xp, yp))

    def shoot(self):
        # Create a new bullet object and add it to the bullets list
        bullet_x = self.xp + math.cos(math.radians(self.ang)) * 80
        bullet_y = self.yp - math.sin(math.radians(self.ang)) * 80
        bullet = Bullet(bullet_x, bullet_y, self.ang)
        self.bullets.append(bullet)

    def move(self):
        x = 0
        y = 0
        # Move up
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            x += math.cos(math.radians(self.ang))
            y -= math.sin(math.radians(self.ang))

        if pygame.key.get_pressed()[pygame.K_d]:
            x += 1

        if pygame.key.get_pressed()[pygame.K_a]:
            x -= 1

        if pygame.key.get_pressed()[pygame.K_q]:
            self.ang += 1

        if pygame.key.get_pressed()[pygame.K_e]:
            self.ang += -1

        self.xp += x
        self.yp += y
        self.sprite = pygame.transform.rotate(self.sprite, self.ang)
        screen.blit(self.sprite, (self.xp, self.yp))