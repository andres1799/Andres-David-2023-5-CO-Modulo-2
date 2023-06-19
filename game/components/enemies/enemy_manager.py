import os.path
import random
import time
#from game.components.Explosion import Explosion
import pygame.mixer

from game.components.enemies.enemy import Enemy
from game.components.enemies.enemyBoss import EnemyBoss
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3, ENEMY_4, SCREEN_HEIGHT, SCREEN_WIDTH, SOUND_EXPLOSION
from game.components.Explosion import Explosion

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.last_enemy_time = time.time()
        self.IMAGE_ENEMY = {0: ENEMY_1, 1: ENEMY_2, 2: ENEMY_3, 3: ENEMY_4}
    def update(self, game):
        self.add_enemy(game)
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self, game):
        enemy_type = self.IMAGE_ENEMY[random.randint(0, 1)]
        if enemy_type == ENEMY_1:
            speed_x = 3
            speed_y = 1
        else:
            speed_x = 5
            speed_y = 1

        """if game.scoremanager.score != 0 and game.scoremanager.score % 10 == 0:
            if len(self.enemies) < 1:
                self.enemies = []
                enemy = Enemy(self.IMAGE_ENEMY[3], speed_x, speed_y)
                self.enemies.append(enemy)"""
        if len(self.enemies) < 2 or time.time() - self.last_enemy_time >= 2:
            enemy = Enemy(self.IMAGE_ENEMY[random.randint(0, 3)], speed_x, speed_y)
            self.enemies.append(enemy)
            self.last_enemy_time = time.time()

    def destroyEnemy(self, bullet, game):
        for enemy in self.enemies:
            if enemy.rect.colliderect(bullet.rect):
                explosion = pygame.mixer.Sound(SOUND_EXPLOSION)
                explosion.set_volume(0.4)
                pygame.mixer.Sound.play(explosion)
                explode = Explosion(enemy.rect.center)
                game.all_sprites.add(explode)
                self.enemies.remove(enemy)
                score = game.scoremanager.update_score()
                game.scoremanager.scorelist(score)
                return True

