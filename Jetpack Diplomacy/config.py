import pygame

pygame.font.init()
pygame.mixer.init()

# Screen
score_height = 50
wall_width = 25
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((sc_width, sc_height))

# Colors
RED = (134, 28, 9)
YELLOW = (212, 169, 65)
WHITE = (255, 255, 255)
GREEN = (0, 127, 33)
BLUE = (0, 97, 148)
DARKER_GREEN = (31, 61, 12)
DARKER_BLUE = (11, 11, 69)


# fps
fps = 60

# Clock
clk = pygame.time.Clock()

# test scenario
scenario1 = pygame.image.load("scenario1.jpeg")

# Bullet
speed_bullet = 1
