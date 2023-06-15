import random
import time
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH
class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.last_enemy_time = time.time()
        self.IMAGE_ENEMY = {0: ENEMY_1, 1: ENEMY_2}
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        enemy_type = self.IMAGE_ENEMY[random.randint(0, 1)]
        if enemy_type == ENEMY_1:
            speed_x = 3
            speed_y = 4
        else:
            speed_x = 5
            speed_y = 6
        if len(self.enemies) < 2: #or time.time() - self.last_enemy_time >= 2:
            enemy = Enemy(self.IMAGE_ENEMY[random.randint(0, 1)], speed_x, speed_y)
            self.enemies.append(enemy)
            self.last_enemy_time = time.time()
    def destroyEnemy(self, bullet):
        for enemy in self.enemies:
            if enemy.rect.colliderect(bullet.rect):
                self.enemies.remove(enemy)
