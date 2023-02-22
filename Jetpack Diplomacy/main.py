from config import *
from game import Game


pygame.init()
play = Game(screen)


play.game_loop()
