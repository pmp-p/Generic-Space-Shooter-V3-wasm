import pygame
from random import randrange
from enemy import Enemy


class Asteroid(Enemy):
    def __init__(self, image, position, width, height):
        super(Asteroid, self).__init__(image, position, width, height)
        self.image = pygame.transform.scale(self.image, (self.width * 8, self.height * 8))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = -self.rect.height
        self.speed_x = randrange(-3, 3)
        self.speed_y = randrange(6, 8)

    def update(self):
        super(Asteroid, self).update()
