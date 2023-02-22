import pygame
from config import *
from pygame import locals


class Game:
    def __init__(self, screen):
        self.menu_looping = menu_looping
        self.screen = screen
        self.background = scenario1
        self.players_sprites = pygame.sprite.Group()
        self.players = []

    def get_screen(self):
        self.background = scenario1

    def start_menu(self):
        if menu_looping:
            screen.blit(start_img_menu, (0, 0))
            pygame.display.update()

    def check_events(self):
        clk.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        self.check_events()
        pygame.display.update()

    def game_loop(self):
        self.get_screen()

        while looping:

            self.start_menu()
            self.check_events()
