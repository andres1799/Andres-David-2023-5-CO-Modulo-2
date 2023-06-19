import random
import pygame
from game.components.power_ups.shield import Shield
from game.components.power_ups.hearth import Heart
from game.components.power_ups.misile import Misile
from game.components.Explosion import Explosion
from game.utils.constants import SPACESHIP_SHIELD, SHIELD_TYPE, SHIELD_SOUND, SOUND_NUCLEAR_BOMB, SOUND_HEALING, HEART_TYPE, MISILE_TYPE

class PowerUpManager():
    MIN_TIME_POWER_UP = 5000
    MAX_TIME_POWER_UP = 10000

    def __init__(self):
        self.power_ups = []
        self.power_up_type = {0: SHIELD_TYPE, 1: HEART_TYPE, 2: MISILE_TYPE}
        self.when_appers = random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        self.duration = random.randint(3, 5)
        self.last_timer = pygame.time.get_ticks()

    def generate_power_up(self):
        eleccion = random.randint(0,2)
        power = self.power_up_type[eleccion]
        if power == SHIELD_TYPE:
            shield = Shield()
            self.power_ups.append(shield)
        elif power == HEART_TYPE:
            heart = Heart()
            self.power_ups.append(heart)
        elif power == MISILE_TYPE:
            misile = Misile()
            self.power_ups.append(misile)
        self.when_appers += random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)




    def update(self, game):
        current_time = pygame.time.get_ticks()
        if len(self.power_ups) == 0 and current_time >= self.when_appers:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                if game.player.power_up_type == SHIELD_TYPE:
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    shieldSound = pygame.mixer.Sound(SHIELD_SOUND)
                    shieldSound.set_volume(0.3)
                    pygame.mixer.Sound.play(shieldSound)
                    self.power_ups = []
                elif game.player.power_up_type == HEART_TYPE:
                    game.player.lives += 1
                    extraLife = pygame.mixer.Sound(SOUND_HEALING)
                    extraLife.set_volume(0.3)
                    pygame.mixer.Sound.play(extraLife)
                    self.power_ups = []
                elif game.player.power_up_type == MISILE_TYPE:
                    for enemy in game.enemy_manager.enemies:
                        explode = Explosion(enemy.rect.center)
                        game.all_sprites.add(explode)
                    nuclearBomb = pygame.mixer.Sound(SOUND_NUCLEAR_BOMB)
                    nuclearBomb.set_volume(0.7)
                    pygame.mixer.Sound.play(nuclearBomb)
                    game.enemy_manager.enemies = []
                    self.power_ups = []

                #self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        power_up = []
        now = pygame.time.get_ticks()
        self.when_appers = random.randint(now + self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)

