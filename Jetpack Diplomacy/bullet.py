from config import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet_img
        self.image = pygame.transform.scale(self.image, (8 * 5, 8 * 5))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
