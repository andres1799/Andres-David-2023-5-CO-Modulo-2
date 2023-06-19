import random
import pygame
from game.components.power_ups.shield import Shield
from game.components.power_ups.hearth import Heart
from game.components.power_ups.misile import Misile
from game.components.Explosion import Explosion
from game.utils.constants import SPACESHIP_SHIELD, SHIELD_TYPE, SHIELD_SOUND

class PowerUpManager():
    MIN_TIME_POWER_UP = 5000
    MAX_TIME_POWER_UP = 10000

    def __init__(self):
        self.power_ups = []
        self.when_appers = random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        self.duration = random.randint(3, 5)

    def generate_power_up(self):
        power_up = Shield()
        heart = Heart()
        misile = Misile()
        self.when_appers += random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        self.power_ups.append(power_up)
        self.power_ups.append(heart)
        self.power_ups.append(misile)

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
                    pygame.mixer.Sound.play(shieldSound)
                    self.power_ups = []
                if game.player.power_up_type == "Heart":
                    game.player.lives += 1
                    self.power_ups = []
                if game.player.power_up_type == "Misile":
                    for enemy in game.enemy_manager.enemies:
                        explode = Explosion(enemy.rect.center)
                        game.all_sprites.add(explode)
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

