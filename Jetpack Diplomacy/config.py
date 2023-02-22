import pygame
from pygame import locals

pygame.font.init()
pygame.mixer.init()

# If True, the game is in loop
looping = True

# Screen
score_height = 50
wall_width = 25
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jetpack-Diplomacy")

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

# Controls
keys = pygame.key.get_pressed()

# test scenario
scenario1 = pygame.image.load("scenario1.jpeg")

# Bullet
speed_bullet = 1

# Menu
menu_looping = True
start_img_menu = pygame.image.load('menu1.jpg')

# Menu
char_looping = False
char_img_menu = pygame.image.load('menu2.jpg')
