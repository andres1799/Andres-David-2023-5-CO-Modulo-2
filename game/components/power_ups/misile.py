import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import MISILE, MISILE_TYPE
class Misile(PowerUp):
    def __init__(self):
        self.size = (30, 50)
        self.image = pygame.transform.scale(MISILE, self.size)
        super().__init__(self.image, MISILE_TYPE)