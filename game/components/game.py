import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, SHIELD_TYPE, MUSIC1, START_SREEN
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.enemies.enemy import Enemy
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.scoreManager import ScoreManager
from game.components.power_ups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu(self.screen)
        self.running = False
        self.scoremanager = ScoreManager()
        self.power_up_manager = PowerUpManager()
        self.all_sprites = pygame.sprite.Group()


    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.scoremanager.score = 0
        self.enemy_manager.enemies = []
        self.bullet_manager.reset()
        self.playing = True
        pygame.mixer.music.load(MUSIC1)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.enemy_manager.update(self)
        self.bullet_manager.update(self, self.enemy_manager)
        self.player.update(user_input, self.bullet_manager)
        self.power_up_manager.update(self)
        self.all_sprites.update()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.all_sprites.draw(self.screen)

        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset(self.screen)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        if self.scoremanager.death_count == 0:
            imageStart = pygame.transform.scale(START_SREEN, (SCREEN_WIDTH, SCREEN_HEIGHT))
            image_height = imageStart.get_height()
            self.screen.blit(imageStart, (self.x_pos_bg, self.y_pos_bg))
            self.screen.blit(imageStart, (self.x_pos_bg, self.y_pos_bg - image_height))



        else:
            pygame.mixer.music.stop()
            image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
            image_height = image.get_height()
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.menu.draw(self.screen, 'Game over. Press any key to restart')
            self.menu.draw(self.screen, f'Your score: {self.scoremanager.score}', half_screen_width, 350, )
            self.menu.draw(self.screen, f'Highest score: {self.scoremanager.highest_score}', half_screen_width, 400, )
            self.menu.draw(self.screen, f'Total deaths: {self.scoremanager.death_count}', half_screen_width, 450, )

        self.menu.update(self)

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.scoremanager.score}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

        fontLives = pygame.font.Font(FONT_STYLE, 30)
        textLives = fontLives.render(f'Lives: {self.player.lives}', True, (255, 255, 255))
        text_rect = textLives.get_rect()
        text_rect.center = (1000, 80)
        self.screen.blit(textLives, text_rect)

    def reset(self):
        self.player.reset()
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                if self.player.power_up_type == SHIELD_TYPE:
                    self.menu.draw(self.screen, f"{self.player.power_up_type.capitalize()} is enables for {time_to_show}", 540, 50, (255, 255, 255))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()


