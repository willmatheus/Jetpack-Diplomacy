import pygame

pygame.font.init()
pygame.mixer.init()

# If True, the game is in loop
looping = True

# Screen
score_height = 50
wall_width = 25
screen_width = 1280
screen_height = 720
PLATFORM_COLOR = (255, 255, 255)
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
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

# game
max_score = 3

# fps
fps = 60

# Clock
clk = pygame.time.Clock()

# Controls
keys = pygame.key.get_pressed()

# test scenario
scenario1 = pygame.image.load("assets/kremlingame.jpg")

# Bullet
speed_bullet = 1

# Menu
menu_looping = True
start_img_menu = pygame.image.load('assets/menu1.jpg')

# Menu char 1
char_looping_1 = False
char_left_img_menu = pygame.image.load('assets/left_menu.jpg')
lenin = pygame.image.load('assets/LENIN8BIT.png')
stalin = pygame.image.load('assets/STALIN8BIT.png')

# Menu char 2
char_looping_2 = False
char_right_img_menu = pygame.image.load('assets/right_menu.jpg')
jfk = pygame.image.load('assets/JFK8BIT.png')
ronald = pygame.image.load('assets/RONALD8BIT.png')

# gameplay loop
gameplay_loop = False
init_players = True
xp1 = 50
yp1 = 50
ang1 = 0
