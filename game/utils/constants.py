import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SOUND_NUCLEAR_BOMB = os.path.join(IMG_DIR, "Sounds/nuclearBomb.mp3")
SOUND_HEALING = os.path.join(IMG_DIR, "Sounds/healingSound.mp3")
SOUND_EXPLOSION = os.path.join(IMG_DIR, "Sounds/explosion.mp3")
SOUND_LASER = os.path.join(IMG_DIR, "Sounds/laser.mp3")
SOUND_LASER_ENEMY = os.path.join(IMG_DIR, "Sounds/laserEnemy.mp3")
MUSIC1 = os.path.join(IMG_DIR, "Sounds/musica1.wav")
SHIELD_SOUND = os.path.join(IMG_DIR, "Sounds/shieldSound.mp3")

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
START_SREEN = pygame.image.load(os.path.join(IMG_DIR, 'Other/StartScreen.png'))


HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
MISILE = pygame.image.load(os.path.join(IMG_DIR, 'Other/destroy.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png"))

FONT_STYLE = 'freesansbold.ttf'
"""
EXPLOSION = []
for i in range(1, 13):
    file = pygame.image.load(os.path.join(IMG_DIR, f"/Explosion/{i}.png"))
    img = pygame.transform.scale(file, (70,70))
    EXPLOSION.append(img)"""
explosion_anim = []
for i in range(1, 13):
    file = 'Explosion/{}.png'.format(i)
    img = pygame.image.load(os.path.join(IMG_DIR, file))#.convert()
    img = pygame.transform.scale(img, (50, 50))
    explosion_anim.append(img)