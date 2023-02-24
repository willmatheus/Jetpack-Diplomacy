from config import *
import math


class Player:
    def __init__(self, sprite, xp, yp, ang):
        self.xp = xp
        self.yp = yp
        self.ang = ang
        self.sprite = sprite
        screen.blit(self.sprite, (xp, yp))

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
        screen.blit(self.sprite, (self.xp, self.yp))
        # return xp, yp
