import pygame
from pygame import mixer
import math

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
angle = 0
ang1 = 0
xp2 = 750
yp2 = 50
ang2 = 0
sprite_speed = 10


class Player:
    def __init__(self, sprite, xp, yp, ang):
        self.xp = xp
        self.yp = yp
        self.ang = ang
        self.sprite = sprite
        # screen.blit(self.sprite, (self.xp, self.yp))

    def draw(self):
        screen.blit(self.sprite, (self.xp, self.yp))

    def move(self):

        # Move up

        if pygame.key.get_pressed()[pygame.K_w]:
            print('rola')
            self.xp += math.cos(math.radians(self.ang))
            self.yp -= math.sin(math.radians(self.ang))
        #    return self.xp, self.yp

        if pygame.key.get_pressed()[pygame.K_d]:
            self.xp += 1

        if pygame.key.get_pressed()[pygame.K_a]:
            self.xp -= 1
        #    return self.xp

        if pygame.key.get_pressed()[pygame.K_q]:
            self.ang += 1
            # return self.ang

        if pygame.key.get_pressed()[pygame.K_e]:
            self.ang += -1
        #    return self.ang

        screen.blit(self.sprite, (self.xp, self.yp))


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.select_char = True
        self.define = True
        self.scenario = scenario1
        self.menu_looping = menu_looping
        self.char_looping_1 = char_looping_1
        self.char_looping_2 = char_looping_2
        self.gameplay_loop = gameplay_loop
        self.background = start_img_menu
        self.players_sprites = pygame.sprite.Group()
        self.players = []

    def get_screen(self):
        self.background = start_img_menu

    def game_loop(self):
        self.get_screen()
        while looping:
            self.get_menu()
            self.draw_sprites()
            pygame.display.update()
            clk.tick(fps)

    def get_menu(self):

        clk.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Exit Press Start
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3 and self.menu_looping:
                    self.menu_looping = False
                    self.char_looping_1 = True

                # Choice P1
                if self.char_looping_1:
                    self.background = char_left_img_menu
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

                        self.select_char = not self.select_char

                    # Confirm P1
                    if event.key == pygame.K_SPACE:
                        self.char_looping_1 = False
                        self.char_looping_2 = True

                        if self.select_char:
                            self.players.append(lenin)
                        else:
                            self.players.append(stalin)
                            print(self.players)

                # Choice p2
                if self.char_looping_2:
                    self.background = char_right_img_menu
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.select_char = not self.select_char

                    # Confirm P2
                    if event.key == pygame.K_0:
                        self.gameplay_loop = True
                        self.char_looping_2 = False
                        if self.select_char:
                            self.players.append(jfk)
                        else:
                            self.players.append(ronald)
                        mixer.music.pause()
                        mixer.init()
                        mixer.music.load('song_game.mp3')
                        mixer.music.set_volume(0.4)
                        mixer.music.play()

                if self.gameplay_loop:
                    self.background = scenario1

    def draw_sprites(self):
        screen.blit(self.background, (0, 0))

        # draw char picker 1
        if self.char_looping_1:
            if self.select_char:
                pygame.draw.circle(self.screen, WHITE, (255, 190), 20)
            else:
                pygame.draw.circle(self.screen, WHITE, (1035, 190), 20)

        # draw char picker 2
        elif self.char_looping_2:
            if self.select_char:
                pygame.draw.circle(self.screen, WHITE, (170, 190), 20)
            else:
                pygame.draw.circle(self.screen, WHITE, (1080, 180), 20)

        elif self.gameplay_loop:
            p1 = Player(self.players[0], xp1, yp1, ang1)
            # p1.draw()
            p1.move()

            mixer.init()
            mixer.music.load('ussr_anthem.mp3')
            mixer.music.set_volume(0.3)
            pygame.init()
            mixer.music.play()

            play = Game(screen)
            play.game_loop()
