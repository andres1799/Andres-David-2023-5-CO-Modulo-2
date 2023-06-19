import pygame
from game.utils.constants import SHIELD_TYPE, SOUND_EXPLOSION
from game.components.Explosion import Explosion


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
    def update(self, game, enemy_manager):
        for enemy in enemy_manager.enemies:
            if enemy.rect.colliderect(game.player.rect):
                if game.player.power_up_type != SHIELD_TYPE:
                    explosion = pygame.mixer.Sound(SOUND_EXPLOSION)
                    explosion.set_volume(0.3)
                    pygame.mixer.Sound.play(explosion)
                    game.player.lives -= 1
                    explode = Explosion(enemy.rect.center)
                    game.all_sprites.add(explode)
                    enemy_manager.enemies.remove(enemy)
                    explode = Explosion(game.player.rect.center)
                    game.all_sprites.add(explode)
                    game.player.hide()
                    if game.player.lives == 0:
                        game.scoremanager.deathCount()
                        game.player.lives = 3
                        game.menu.actualscreen = True
                        game.playing = False
                        pygame.time.delay(1000)
                        break
                else:
                    enemy_manager.enemies.remove(enemy)
                    explode = Explosion(enemy.rect.center)
                    game.all_sprites.add(explode)

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    explosion = pygame.mixer.Sound(SOUND_EXPLOSION)
                    explosion.set_volume(0.3)
                    pygame.mixer.Sound.play(explosion)
                    explode = Explosion(game.player.rect.center)
                    game.all_sprites.add(explode)
                    game.player.hide()
                    game.player.lives -= 1
                    if game.player.lives == 0:
                        game.scoremanager.deathCount()
                        game.player.lives = 3
                        game.menu.actualscreen = True
                        game.playing = False
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
        if bullet.owner == "enemy":
            self.enemy_bullets.append(bullet)

        elif bullet.owner == "player":
            self.bullets.append(bullet)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []