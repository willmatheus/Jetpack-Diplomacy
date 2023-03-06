<<<<<<< HEAD
import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, color, dimensions, coordinates):
        super().__init__()
        self.image = pygame.Surface(dimensions)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=coordinates)
=======
import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, color, dimensions, coordinates):
        super().__init__()
        self.image = pygame.Surface(dimensions)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=coordinates)
>>>>>>> 0a13bb8fc13d96a35b073e643ba90dfbe4e56348
