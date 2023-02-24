from config import *
import math


class Player:
    def __init__(self, sprite, xp, yp, ang):
        self.xp = xp
        self.yp = yp
        self.ang = ang
        self.sprite = sprite

    def spawn(self):
        screen.blit(self.sprite, (xp, yp))

    def move(keys, xp, yp, ang):
        # Move up

        if keys[pygame.K_w]:
            xp += math.cos(math.radians(ang))
            yp -= math.sin(math.radians(ang))
            return xp, yp, ang

        if keys[pygame.K_d]:
            xp += 1
            return xp

        if keys[pygame.K_a]:
            xp -= 1
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

        if keys[pygame.K_SEMICOLON]:
            menu_looping = False
            return menu_looping
