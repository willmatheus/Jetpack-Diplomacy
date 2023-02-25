from config import *
from game import *
from pygame import mixer

mixer.init()
mixer.music.load('assets/ussr_anthem.mp3')
mixer.music.set_volume(0.3)
pygame.init()
mixer.music.play()

play = Game(screen)
play.game_loop()
