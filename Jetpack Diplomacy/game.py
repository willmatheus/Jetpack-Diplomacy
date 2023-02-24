import pygame.key
from player import Player
from config import *
from pygame import mixer
import math


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
        self.xp1 = xp1
        self.yp1 = yp1
        self.ang1 = ang1
        self.xp2 = xp2
        self.yp2 = yp2
        self.ang2 = ang2

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
                        mixer.music.load('assets/song_game.mp3')
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
            p1 = Player(self.players[0], self.xp1, self.yp1, self.ang1)
            p2 = Player(self.players[1], self.xp2, self.yp2, self.ang2)

            # Gravity
            if self.yp1 < 530:
                self.yp1 += gravity
            else:
                self.yp1 = 530

            if self.yp2 > 530:
                self.yp2 += gravity
            else:
                self.yp2 = 530

            if pygame.key.get_pressed()[pygame.K_w]:
                self.xp1 += math.cos(math.radians(self.ang1))
                self.yp1 -= math.sin(math.radians(self.ang1))

            if pygame.key.get_pressed()[pygame.K_d]:
                self.xp1 += p_speed

            if pygame.key.get_pressed()[pygame.K_a]:
                self.xp1 -= p_speed

            if pygame.key.get_pressed()[pygame.K_q]:
                self.ang1 += 1

            if pygame.key.get_pressed()[pygame.K_e]:
                self.ang1 += -1

            if pygame.key.get_pressed()[pygame.K_UP]:
                self.xp2 += p_speed * math.cos(math.radians(self.ang2))
                self.yp2 -= p_speed * math.sin(math.radians(self.ang2))

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.xp2 += p_speed

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.xp2 -= p_speed

            if pygame.key.get_pressed()[pygame.K_SEMICOLON]:
                self.ang2 += 1

            if pygame.key.get_pressed()[pygame.K_9]:
                self.ang2 += -1
