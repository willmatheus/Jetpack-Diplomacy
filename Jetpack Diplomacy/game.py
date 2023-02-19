from config import *


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.background = scenario1
        self.players_sprites = pygame.sprite.Group()
        self.players = []

    def get_screen(self):
        self.background = scenario1

    def game_loop(self):
        self.get_screen()

    def check_events(self):
        clk.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        self.check_events()
        pygame.display.update()