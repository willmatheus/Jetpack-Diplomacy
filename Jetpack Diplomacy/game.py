from config import *


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.menu_looping = menu_looping
        self.char_looping = char_looping
        self.background = start_img_menu
        self.background2 = char_img_menu
        self.players_sprites = pygame.sprite.Group()
        self.players = []

    def get_screen(self):
        self.background = start_img_menu

    def game_loop(self):
        self.get_screen()

        while looping:
            self.check_events()
            self.draw_sprites()
            pygame.display.update()
            clk.tick(fps)

    def check_events(self):
        clk.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


    def draw_sprites(self):
        screen.blit(self.background, (0, 0))
        
