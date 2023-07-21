import pygame

from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT //2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH //2

    def __init__(self, message, screen, score=0, best_score = 0):  # Agregar el parámetro score
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

        self.score = score  # Almacenar el puntaje recibido
        self.best_score = best_score

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)


        # Mostrar el puntaje debajo del mensaje de "Game Over"
        score_text = self.font.render(f'Score: {self.score}', True, (0, 0, 0))
        score_rect = score_text.get_rect()
        score_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 40)
        screen.blit(score_text, score_rect)

        best_score_text = self.font.render(f'Best Score: {self.best_score}', True, (0, 0, 0))
        best_score_rect = best_score_text.get_rect()
        best_score_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 80)
        screen.blit(best_score_text, best_score_rect)


    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def update_message(self, message, score=0, best_score = 0):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
    
        self.score = score  # Actualizar el puntaje recibido
        self.best_score = best_score

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))