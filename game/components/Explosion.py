import pygame.time

from game.utils.constants import EXPLOSION
class Explosion:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
    def draw_explosion(self, screen):
        for img in EXPLOSION:
            print("Easdas")
            screen.blit(self.image, self.rect)