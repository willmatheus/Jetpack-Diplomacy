from config import *
import math
import game


class Bullet:
    def __init__(self, x, y, angle):
        self.angle = angle
        self.speed = 10
        self.radius = 3
    #    self.rect = 0
        self.screen = screen
        self.x = x
        self.y = y
        self.dx = self.speed * math.cos(math.radians(self.angle))
        self.dy = self.speed * -math.sin(math.radians(self.angle))

    def shoot(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.radius, self.radius))
        self.x = self.x + self.dx
        self.y = self.y + self.dy


def check_collision(self, bullets):
        # Check if any bullet in the list collides with this player
        for bullet in bullets:
            dist = math.sqrt((bullet.x - self.xp)**2 + (bullet.y - self.yp)**2)
            if dist < bullet.radius + 50:  # assuming player size is 100x100
                # collision detected
                return True
        return False
