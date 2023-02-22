import pygame
from config import *
from pygame import locals
from players import Player


class Game:
    def __init__(self, screen):
        self.menu_looping = menu_looping
        self.char_looping = char_looping
        self.screen = screen
        self.background = start_img_menu
        self.players_sprites = pygame.sprite.Group()
        self.players = []

    def get_screen(self):
        screen.blit(self.background, (0, 0))
        pygame.display.update()

    def check_events(self):

        clk.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_KP_ENTER and menu_looping:
                    self.menu_looping = False
                    self.char_looping = True
                    self.background = char_img_menu
                    self.get_screen()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

    def game_loop(self):

        while looping:
            self.get_screen()
            self.check_events()
