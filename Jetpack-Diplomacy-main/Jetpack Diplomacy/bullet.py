from config import *
import math
import game


class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 10
        self.radius = 3

    def move_bullet(self):
        self.x += math.cos(math.radians(self.angle)) * self.speed
        self.y -= math.sin(math.radians(self.angle)) * self.speed
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)

    def shoot(self):
        # Create a new bullet object and add it to the bullets list
        bullet_x = self.xp + math.cos(math.radians(self.ang)) * 80
        bullet_y = self.yp - math.sin(math.radians(self.ang)) * 80
        bullet = Bullet(bullet_x, bullet_y, self.ang)
        self.bullets.append(bullet)

    def check_collision(self, bullets):
        # Check if any bullet in the list collides with this player
        for bullet in bullets:
            dist = math.sqrt((bullet.x - self.xp)**2 + (bullet.y - self.yp)**2)
            if dist < bullet.radius + 50:  # assuming player size is 100x100
                # collision detected
                return True
        return False
