from config import *
import math


class Player:
    def __init__(self, sprite, xp, yp, ang):
        self.xp = xp
        self.yp = yp
        self.ang = ang
        self.sprite = sprite
        #screen.blit(self.sprite, (self.xp, self.yp))

    def draw(self):
        screen.blit(self.sprite, (self.xp, self.yp))

    def move(self):


        # Move up

        if pygame.key.get_pressed()[pygame.K_w]:
            print('rola')
            self.xp += math.cos(math.radians(self.ang))
            self.yp -= math.sin(math.radians(self.ang))
        #    return self.xp, self.yp

        if pygame.key.get_pressed()[pygame.K_d]:
            self.xp += 1

        if pygame.key.get_pressed()[pygame.K_a]:
            self.xp -= 1
        #    return self.xp

        if pygame.key.get_pressed()[pygame.K_q]:
            self.ang += 1
            #return self.ang

        if pygame.key.get_pressed()[pygame.K_e]:
            self.ang += -1
        #    return self.ang

        screen.blit(self.sprite, (self.xp, self.yp))
