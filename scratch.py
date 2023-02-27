import pygame
from pygame import joystick
pygame.init()
joystick.init()

pygame.display.set_mode((100, 200))

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.JOYBUTTONDOWN:
            #print(pygame.joystick.Joystick(0).get_button())
            print(event)

        if event.type == pygame.JOYAXISMOTION:
            print(event)

        if event.type == pygame.JOYBUTTONUP:
            print(event)