from config import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, vel_x, vel_y):
        super().__init__()
        self.player = player
        self.x = player.rect.x
        self.y = player.rect.y
        self.image = bullet
        self.image = pygame.transform.scale(self.image, (8 * 5, 8 * 5))
        self.group = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]
        self.dx = vel_x
        self.dy = vel_y

    def update(self):
        self.move()

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
