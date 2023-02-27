import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def update(self):
        self.rect.move_ip(*self.speed)

    def collide_with_wall(self, wall_rect):
        if self.rect.colliderect(wall_rect):
            self.kill()  # Remove the bullet from all sprite groups

bullet_group = pygame.sprite.Group()
bullet = Bullet((100, 100), (5, 0))
bullet_group.add(bullet)

wall_rect = pygame.Rect(0, 0, 1280, 720)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    bullet_group.update()
    screen.fill((0, 0, 0))
    bullet_group.draw(screen)
    bullet.collide_with_wall(wall_rect)
    pygame.display.update()
    clock.tick(60)
