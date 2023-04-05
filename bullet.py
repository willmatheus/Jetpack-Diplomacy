from config import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 9
        self.image = bullet_img
        self.image = pygame.transform.scale(self.image, (8 * 5, 8 * 5))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        # move bullet
        self.rect.x += (self.direction * self.speed)
        # check if bullet has gone of the screen
        if self.rect.right < 0 or self.rect.left > screen_width:
            self.kill()
