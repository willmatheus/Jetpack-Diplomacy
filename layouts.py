<<<<<<< HEAD
import wall
from config import *


class Layouts:
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.wall_color = RED
        self.obstacles()

    def get_group(self):
        return self.group


    def obstacles(self):
        self.group.add(wall.Wall(self.wall_color, (20, 320), (640, 0)))
        self.group.add(wall.Wall(self.wall_color, (20, 320), (900, 420)))
        self.group.add(wall.Wall(self.wall_color, (20, 320), (320, 420)))
        self.group.add(wall.Wall(self.wall_color, (1280, 20), (0, 700)))
=======
import wall
from config import *


class Layouts:
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.wall_color = RED
        self.obstacles()

    def get_group(self):
        return self.group


    def obstacles(self):
        self.group.add(wall.Wall(self.wall_color, (20, 320), (640, 0)))
        self.group.add(wall.Wall(self.wall_color, (20, 320), (900, 420)))
        self.group.add(wall.Wall(self.wall_color, (20, 320), (320, 420)))
        self.group.add(wall.Wall(self.wall_color, (1280, 20), (0, 700)))
>>>>>>> 0a13bb8fc13d96a35b073e643ba90dfbe4e56348
