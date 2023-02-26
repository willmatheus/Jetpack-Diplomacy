import pygame.key
from player import Player
from config import *
from pygame import mixer


class Game(pygame.sprite.Sprite):
    def __init__(self, screen_game):
        super().__init__()
        self.screen = screen_game
        self.gameplay_loop = gameplay_loop
        self.select_char = True
        self.menu_looping = menu_looping
        self.char_looping_1 = char_looping_1
        self.char_looping_2 = char_looping_2
        self.background = start_img_menu
        self.players = []
        self.players.append(Player(xp1, yp1, lenin))
        self.players.append(Player(xp2, yp2, stalin))
        self.moving_left = False
        self.moving_right = False

    def get_screen(self):
        self.background = scenario1

    def game_loop(self):
        self.get_screen()
        while looping:
            self.check_events_game()
            self.draw_sprites()
            pygame.display.update()
            clk.tick(fps)

    def check_shoot(self):

        if pygame.sprite.spritecollide(self.players[0], self.players[0].bullet_group, False):
            if self.players[1].alive:
                self.players[1].kill()

    def check_events_game(self):
        # move players
        if self.alive:
            self.players[0].move(self.moving_left, self.moving_right)
            if self.players[0].shoot:
                self.players[0].shoot_()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.moving_left = True
                if event.key == pygame.K_d:
                    self.moving_right = True
                if event.key == pygame.K_SPACE:
                    self.players[0].shoot = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.moving_left = False
                if event.key == pygame.K_d:
                    self.moving_right = False
                if event.key == pygame.K_SPACE:
                    self.players[0].shoot = False

            if event.type == pygame.QUIT:
                exit()

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

            # draw char

        self.players[0].draw()
        self.players[1].draw()
        # draw and update bullets on screen
        self.players[0].bullet_group.update()
        self.players[0].bullet_group.draw(self.screen)
        self.players[0].update()
