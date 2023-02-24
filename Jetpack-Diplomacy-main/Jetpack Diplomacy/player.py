from config import *
import math


class Player:
    def __init__(self, sprite, xp, yp, ang):
        self.xp = xp
        self.yp = yp
        self.ang = ang
        self.sprite = sprite

    def draw(self):
        screen.blit(self.sprite, (self.xp, self.yp))

    def move(self):
        # Move up
        if keys[pygame.K_w]:
            self.xp += math.cos(math.radians(self.ang))
            self.yp -= math.sin(math.radians(self.ang))

        if keys[pygame.K_d]:
            self.xp += 1
            return self.xp

        if keys[pygame.K_a]:
            self.xp -= 1
            return xp

        if keys[pygame.K_q]:
            ang += 1
            return xp, yp, ang

        if keys[pygame.K_e]:
            ang += -1
            return xp, yp, ang

        if keys[pygame.K_r]:
            ang += -1
            return xp, yp, ang
