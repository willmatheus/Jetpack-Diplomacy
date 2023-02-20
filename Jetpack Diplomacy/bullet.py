import math
from config import *
import pygame


class Bullet:
    def __init__(self, xp, yp, angle, color_bullet):
        self.angle = angle
        self.rect = pygame.Rect(25 + xp + 25 * math.cos(math.radians(self.angle)), 25 + yp - 25 * math.sin(math.radians(self.angle)), 5, 5)
        self.dx = speed_bullet * math.cos(math.radians(self.angle))
        self.dy = speed_bullet * -math.sin(math.radians(self.angle))
        self.color = color_bullet

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        rect = pygame.Rect(self.rect.x, self.rect.y, 5, 5)
        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy
        self.draw()
