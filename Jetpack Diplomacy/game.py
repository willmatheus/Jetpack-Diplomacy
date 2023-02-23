import pygame
from config import *
from pygame import locals
from players import Player


class Game:
    def __init__(self, screen):

        self.menu_looping = menu_looping
        self.char_looping_1 = char_looping_1
        self.select_char = True
        self.char_looping_2 = char_looping_2
        self.main_loop = main_loop
        self.screen = screen
        self.background = start_img_menu
        self.players_sprites = pygame.sprite.Group()
        self.players = []

    def get_screen(self):
        screen.blit(self.background, (0, 0))

        if self.char_looping_1:
            if self.select_char:
                pygame.draw.circle(self.screen, WHITE, (255, 190), 20)
            else:
                pygame.draw.circle(self.screen, WHITE, (1035, 190), 20)

        elif self.char_looping_2:
            if self.select_char:
                pygame.draw.circle(self.screen, WHITE, (170, 190), 20)
            else:
                pygame.draw.circle(self.screen, WHITE, (1080, 180), 20)

        pygame.display.update()

    def check_events(self):

        clk.tick(60)

        for event in pygame.event.get():

            # User Interaction
            if event.type == pygame.KEYDOWN:

                # Press Start Menu to Left Player Char Menu
                if event.key == pygame.K_KP_ENTER and self.menu_looping:
                    self.menu_looping = False
                    self.char_looping_1 = True

                # First Player choice char
                if self.char_looping_1:
                    # Change img
                    self.background = char_left_img_menu
                    self.get_screen()

                    # Select char
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.select_char = not self.select_char

                    # Confirm
                    if event.key == pygame.K_SPACE:
                        self.char_looping_1 = False
                        self.char_looping_2 = True

                # Second Player choice char
                if self.char_looping_2:
                    # Load img
                    self.background = char_right_img_menu
                    self.get_screen()

                    # Select
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.select_char = not self.select_char

                    # Confirm
                    if event.key == pygame.K_0:
                        self.main_loop = True
                        self.char_looping_2 = False

                # If in game, Change BG
                if self.main_loop:
                    self.background = game_bg
                    self.get_screen()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

    def game_loop(self):

        while looping:

            self.get_screen()
            self.check_events()

            pygame.display.update()
