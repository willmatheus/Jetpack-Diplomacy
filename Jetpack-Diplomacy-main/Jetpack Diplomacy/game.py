import pygame.key
from pygame import mixer
import obstacles
from config import *
from player import Player


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
        self.per1_1_left = True
        self.per1_2_left = True
        self.per1_1_right = True
        self.per1_2_right = True
        self.per1_1_vert = True
        self.per1_2_vert = True
        self.per2_1_left = True
        self.per2_2_left = True
        self.per2_1_right = True
        self.per2_2_right = True
        self.per2_1_vert = True
        self.per2_2_vert = True

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
        global p_speed
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

            obstacles.draw_platform()
            p1 = Player(self.players[0], self.xp1, self.yp1, self.ang1)
            p2 = Player(self.players[1], self.xp2, self.yp2, self.ang2)
            # shoot bullets when r and return are pressed
            if pygame.key.get_pressed()[pygame.K_r]:
                p1.shoot()
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                p2.shoot()
            for bullet in p1.bullets + p2.bullets:
                bullet.move_bullet()

            # Gravity
            if self.yp1 < 560 and self.per1_2_vert:
                self.yp1 += gravity

            if self.yp2 < 560 and self.per2_2_vert:
                self.yp2 += gravity

            # collision with walls
            if self.xp1 >= 1070:
                self.xp1 = 1070

            if self.xp1 <= - 20:
                self.xp1 = - 20

            if self.xp2 >= 1050:
                self.xp2 = 1050

            if self.xp2 <= - 20:
                self.xp2 = - 20

            if self.yp1 <= 0:
                self.yp1 = 0

            if self.yp2 <= 0:
                self.yp2 = 0

            if (self.xp1 >= 162 and self.xp1 <= 180) and (self.yp1 >= 0 and self.yp1 <= 320):
                self.per1_1_left = False
            else:
                self.per1_1_left = True

            if (self.xp1 >= 762 and self.xp1 <= 780) and (self.yp1 >= 250 and self.yp1 <= 720):
                self.per1_2_left = False
            else:
                self.per1_2_left = True

            if (self.xp1 >= 258 and self.xp1 <= 270) and (self.yp1 >= 0 and self.yp1 <= 320):
                self.per1_1_right = False
            else:
                self.per1_1_right = True

            if (self.xp1 >= 858 and self.xp1 <= 870) and (self.yp1 >= 250 and self.yp1 <= 720):
                self.per1_2_right = False
            else:
                self.per1_2_right = True

            if (self.xp1 >= 192 and self.xp1 <= 270) and (self.yp1 >= 310 and self.yp1 <= 330):
                self.per1_1_vert = False
            else:
                self.per1_1_vert = True

            if (self.xp1 >= 770 and self.xp1 <= 880) and (self.yp1 >= 245 and self.yp1 <= 275):
                self.per1_2_vert = False
            else:
                self.per1_2_vert = True

            if (self.xp2 >= 162 and self.xp2 <= 180) and (self.yp2 >= 0 and self.yp2 <= 320):
                self.per2_1_left = False
            else:
                self.per2_1_left = True

            if (self.xp2 >= 762 and self.xp2 <= 780) and (self.yp2 >= 250 and self.yp2 <= 720):
                self.per2_2_left = False
            else:
                self.per2_2_left = True

            if (self.xp2 >= 258 and self.xp2 <= 270) and (self.yp2 >= 0 and self.yp2 <= 320):
                self.per2_1_right = False
            else:
                self.per2_1_right = True

            if (self.xp2 >= 858 and self.xp2 <= 870) and (self.yp2 >= 250 and self.yp2 <= 720):
                self.per2_2_right = False
            else:
                self.per2_2_right = True

            if (self.xp2 >= 192 and self.xp2 <= 270) and (self.yp2 >= 310 and self.yp2 <= 330):
                self.per2_1_vert = False
            else:
                self.per2_1_vert = True

            if (self.xp2 >= 770 and self.xp2 <= 880) and (self.yp2 >= 245 and self.yp2 <= 275):
                self.per2_2_vert = False
            else:
                self.per2_2_vert = True

            # movement
            if pygame.key.get_pressed()[pygame.K_d] and self.per1_1_left and self.per1_2_left:
                self.xp1 += p_speed

            if pygame.key.get_pressed()[pygame.K_a] and self.per1_1_right and self.per1_2_right:
                self.xp1 -= p_speed

            if pygame.key.get_pressed()[pygame.K_q]:
                self.ang1 += 1

            if pygame.key.get_pressed()[pygame.K_e]:
                self.ang1 += -1

            if pygame.key.get_pressed()[pygame.K_RIGHT] and self.per2_1_left and self.per2_2_left:
                self.xp2 += p_speed

            if pygame.key.get_pressed()[pygame.K_LEFT] and self.per2_1_right and self.per2_2_right:
                self.xp2 -= p_speed

            if pygame.key.get_pressed()[pygame.K_8]:
                self.ang2 += 1

            if pygame.key.get_pressed()[pygame.K_9]:
                self.ang2 += -1

            # jetpack
            if pygame.key.get_pressed()[pygame.K_SPACE] and self.per1_1_vert:
                self.yp1 -= 15
            if pygame.key.get_pressed()[pygame.K_k] and self.per2_1_vert:
                self.yp2 -= 15
