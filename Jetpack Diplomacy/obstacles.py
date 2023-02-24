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
floor = Platform(PLATFORM_COLOR, screen_width, PLATFORM_HEIGHT, 0, screen_height - PLATFORM_HEIGHT)
platform1 = Platform(PLATFORM_COLOR, PLATFORM_WIDTH, PLATFORM_HEIGHT, screen_width // 4,
                     screen_height - PLATFORM_HEIGHT - 100)
platform2 = Platform(PLATFORM_COLOR, PLATFORM_WIDTH, PLATFORM_HEIGHT, 3 * screen_width // 4 - PLATFORM_WIDTH,
                     screen_height - PLATFORM_HEIGHT - 200)

# Create a group to hold the platforms
platform_group = pygame.sprite.Group()
platform_group.add(floor, platform1, platform2)

# Draw the platforms on the screen
platform_group.draw(screen)

# Update the display
pygame.display.flip()

# Control the frame rate
clock.tick(60)
