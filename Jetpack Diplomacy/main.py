from config import *
from game import Game


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jetpack-Diplomacy")
play = Game(screen)


play.game_loop()
