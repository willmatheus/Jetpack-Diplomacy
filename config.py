<<<<<<< HEAD
import pygame

pygame.font.init()
pygame.mixer.init()

# If True, the game is in loop
looping = True

# gravity
gravity = 0.3

# font
score_font = pygame.font.Font('assets/PixeloidMono.ttf', 100)

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
max_score = 5

# fps
fps = 60

# Clock
clk = pygame.time.Clock()

# timers
shoot_t = 10
defeat_time = 50

# scenario
scenario1 = pygame.image.load("assets/kremlingame.jpg")

# optional screens
player1_wins = pygame.image.load("assets/PLAYER1WINS.jpg")
player2_wins = pygame.image.load("assets/PLAYER2WINS.jpg")

# Bullet
speed_bullet = 1

# Menu
menu_looping = True
start_img_menu = pygame.image.load('assets/menu1.jpg')

# Menu char 1
char_looping_1 = False
char_left_img_menu = pygame.image.load('assets/left_menu.jpg')

# Menu char 2
char_looping_2 = False
char_right_img_menu = pygame.image.load('assets/right_menu.jpg')

# sprites
lenin = pygame.image.load('assets/lenin_with_jetpack.png')
stalin32 = pygame.image.load('assets/stalin22-removebg-preview.png')
jfk = pygame.image.load('assets/jfk_with_jetpack.png')
ronald = pygame.image.load('assets/ronald_with_jetpack.png')
bullet_img = pygame.image.load("assets/testeball.png")

# gameplay loop
gameplay_loop = False

# coordinates
xp1 = 50
yp1 = 0
xp2 = 750
yp2 = 0
speed = 10

jetpack = pygame.mixer.Sound('assets/jetpack_sound.wav')
=======
import pygame

pygame.font.init()
pygame.mixer.init()

# If True, the game is in loop
looping = True

# gravity
gravity = 0.3

# font
score_font = pygame.font.Font('assets/PixeloidMono.ttf', 100)

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
max_score = 5

# fps
fps = 60

# Clock
clk = pygame.time.Clock()

# timers
shoot_t = 10
defeat_time = 50

# scenario
scenario1 = pygame.image.load("assets/kremlingame.jpg")

# optional screens
player1_wins = pygame.image.load("assets/PLAYER1WINS.jpg")
player2_wins = pygame.image.load("assets/PLAYER2WINS.jpg")

# Bullet
speed_bullet = 1

# Menu
menu_looping = True
start_img_menu = pygame.image.load('assets/menu1.jpg')

# Menu char 1
char_looping_1 = False
char_left_img_menu = pygame.image.load('assets/left_menu.jpg')

# Menu char 2
char_looping_2 = False
char_right_img_menu = pygame.image.load('assets/right_menu.jpg')

# sprites
lenin = pygame.image.load('assets/lenin_with_jetpack.png')
stalin = pygame.image.load('assets/stalin_with_jetpack.png')
jfk = pygame.image.load('assets/jfk_with_jetpack.png')
ronald = pygame.image.load('assets/ronald_with_jetpack.png')
bullet_img = pygame.image.load("assets/testeball.png")

# gameplay loop
gameplay_loop = False

# coordinates
xp1 = 50
yp1 = 0
xp2 = 750
yp2 = 0
speed = 10

jetpack = pygame.mixer.Sound('assets/jetpack_sound.wav')
>>>>>>> 0a13bb8fc13d96a35b073e643ba90dfbe4e56348
