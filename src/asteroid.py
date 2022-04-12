import pygame
from random import randrange
from enemy import Enemy


class Asteroid(Enemy):
    def __init__(self, image, position, width, height):
        super().__init__(image, position, width, height)
        self.image = pygame.transform.scale(self.image, (self.width * 2.3, self.height * 2.3))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = 95
        self.speed_x = randrange(-3, 3)
        self.speed_y = randrange(1, 4)

    def update(self):
        super().update()
