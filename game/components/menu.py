import pygame.font
from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT, START_SREEN

class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    def __init__(self, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.actualscreen = False
        self.score = 0
        self.highscore = 0
        self.deaths = 0

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen, message, x = HALF_SCREEN_WIDTH, y = HALF_SCREEN_HEIGHT, color = (255, 255, 255)):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y - 100)
        screen.blit(text, text_rect)

    def handle_events_on_menu(self, game):
        user_input = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif user_input[pygame.K_RETURN]:
                game.run()
    def reset(self, screen):
        screen.fill((255, 255, 255))

    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH + 20, self.HALF_SCREEN_HEIGHT)


