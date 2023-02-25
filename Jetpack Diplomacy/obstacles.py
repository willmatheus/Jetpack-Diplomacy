from config import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()

        # Create a white rectangle for the platform with the specified width and height
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Set the position of the platform to the specified location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Set up the clock to control the game's frame rate
clock = pygame.time.Clock()

# Create the floor and two platforms
platform1 = Platform(WHITE, 20, 320, 300, 0)
platform2 = Platform(WHITE, 20, 320, 900, 420)
# Create a group to hold the platforms
platform_group = pygame.sprite.Group()
platform_group.add(platform1, platform2)


# Draw the platforms on the screen
def draw_platform():
    platform_group.draw(screen)


# Update the display
pygame.display.flip()

# Control the frame rate
clock.tick(60)