import random
import time
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH
class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.last_enemy_time = time.time()
        self.IMAGE_ENEMY = {0: ENEMY_1, 1: ENEMY_2}
    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    def add_enemy(self):
        if len(self.enemies) < 1 or time.time() - self.last_enemy_time >= 7:
            self.speed_y = random.randint(1,5)
            self.speed_x = random.randint(1,8)
            enemy = Enemy(self.IMAGE_ENEMY[random.randint(0,1)], self.speed_x, self.speed_y)
            self.enemies.append(enemy)
            self.last_enemy_time = time.time()
