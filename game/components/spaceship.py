import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE, SOUND_LASER
from game.components.bullets.bullet import Bullet
class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGTH = 60
    SPEED = 10
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    X_POS = (SCREEN_WIDTH // 2) - SPACESHIP_WIDTH
    Y_POS = 500

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH,self.SPACESHIP_HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0
        self.lives = 3
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def update(self, user_input, bullet_manager):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 40)
        key_actions = {
            pygame.K_LEFT: lambda: self.move_left(),
            pygame.K_RIGHT: self.move_right,
            pygame.K_UP: self.move_up,
            pygame.K_DOWN: self.move_down,
            pygame.K_j: lambda: self.shoot(bullet_manager)
        }
        for key, action in key_actions.items():
            if user_input[key]:
                action()

    def move_left(self):
        self.rect.x -= self.SPEED
        if self.rect.left < -self.SPACESHIP_WIDTH:
            self.rect.x += SCREEN_WIDTH + self.SPACESHIP_WIDTH

    def move_right(self):
        self.rect.x += self.SPEED
        if self.rect.right > SCREEN_WIDTH + self.SPACESHIP_WIDTH:
            self.rect.x -= SCREEN_WIDTH + self.SPACESHIP_WIDTH

    def move_up(self):
        if self.rect.y > self.HALF_SCREEN_HEIGHT:
            self.rect.y -= self.SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - self.SPACESHIP_HEIGTH:
            self.rect.y += self.SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self)
            laser = pygame.mixer.Sound(SOUND_LASER)
            pygame.mixer.Sound.play(laser)
            bullet_manager.add_bullet(bullet)

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.power_time_up = 0
        self.power_up_type = DEFAULT_TYPE

    def set_image(self, size = (40, 60), image = SPACESHIP):
        self.image = pygame.transform.scale(image, size)

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT + 200)

