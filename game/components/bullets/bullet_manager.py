import pygame
from game.utils.constants import SHIELD_TYPE, SOUND_LASER, SOUND_LASER_ENEMY
from game.components.Explosion import Explosion


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
    def update(self, game, enemy_manager):
        for enemy in enemy_manager.enemies:
            if enemy.rect.colliderect(game.player.rect):
                if game.player.power_up_type != SHIELD_TYPE:
                    game.player.lives -= 1

                    explode = Explosion(enemy.rect.center)
                    game.all_sprites.add(explode)

                    enemy_manager.enemies.remove(enemy)

                    explode = Explosion(game.player.rect.center)
                    game.all_sprites.add(explode)
                    if game.player.lives == 0:
                        game.scoremanager.deathCount()
                        game.player.lives = 3
                        game.menu.actualscreen = True
                        game.playing = False
                        pygame.time.delay(1000)
                        break
                else:
                    enemy_manager.enemies.remove(enemy)

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.player.lives -= 1
                    explode = Explosion(game.player.rect.center)
                    game.all_sprites.add(explode)
                    if game.player.lives == 0:
                        game.scoremanager.deathCount()
                        game.player.lives = 3
                        game.menu.actualscreen = True
                        game.playing = False
                        break
            else:
                break

        for bullet in self.bullets:
            bullet.update(self.bullets)
            enemy = enemy_manager.destroyEnemy(bullet, game)
            if enemy:
                self.bullets.remove(bullet)

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            laser = pygame.mixer.Sound(SOUND_LASER_ENEMY)
            pygame.mixer.Sound.play(laser)
            self.enemy_bullets.append(bullet)

        elif bullet.owner == 'player' or\
                len(self.bullets) < 1:
            laser = pygame.mixer.Sound(SOUND_LASER)
            pygame.mixer.Sound.play(laser)
            self.bullets.append(bullet)