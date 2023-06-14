import random
import pygame
import time
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGTH = 60
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
    Y_POS = 10
    seed = int(time.time())
    random.seed(seed)

    MOV_X = {0: 'left', 1: 'right'}
    def __init__(self, image_enemy, speed_x, speed_y):
        self.image = pygame.transform.scale(image_enemy, (self.ENEMY_WIDTH, self.ENEMY_HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 18)]
        self.rect.y = self.Y_POS
        self.speed_x = speed_x[0] if image_enemy == ENEMY_1 else speed_x[1]
        self.speed_y = speed_y[0] if image_enemy == ENEMY_1 else speed_y[1]
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 200)
        self.index = 0

    def update(self, ships):
        self.rect.y += self.speed_y
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            self.rect.y -= SCREEN_HEIGHT
            #ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and  self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0
