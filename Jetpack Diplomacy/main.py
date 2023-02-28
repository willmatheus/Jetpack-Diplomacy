from config import *
from game import Game
from pygame import mixer

mixer.init()
mixer.music.load('assets/ussr_anthem.mp3')
mixer.music.set_volume(0.3)
pygame.init()
pygame.joystick.init()
mixer.music.play()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jetpack-Diplomacy")
play = Game(screen)
play.game_loop()
