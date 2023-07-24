import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemy_manager import EnemyManager
from game.components.menu.menu import Menu
from game.components.meteorite.meteorite_manager import MeteoriteManager
from game.components.power_ups.power_up_manager import PowerUpManager

from game.utils.constants import BG, FONT_STYLE, ICON, NEW_BG, RESET, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship
from sys import exit

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
        self.running = False
        self.menu = Menu('Press any key to start...', self.screen)
        self.death_count = 0
        self.score = 0
        self.highest_score = 0
        self.power_up_manager = PowerUpManager()
        self.meteorite_manager = MeteoriteManager()

    def execute(self):  
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.score = 0
        self.enemy_manager.reset()
        self.meteorite_manager.reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                exit()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.meteorite_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.meteorite_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()

    def draw_background(self):
        if self.score % 3 == 0:
            # Cambiar el fondo cuando el score es múltiplo de 3
            image = pygame.transform.scale(NEW_BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        else:
            image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed


    
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)   
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if not self.death_count:
            icon = self.image = pygame.transform.scale(ICON, (80, 120))
            self.screen.blit(icon, (half_screen_width - 50, half_screen_height - 150))
            self.menu.draw(self.screen)
        else:
          self.update_highest_score()
          icon = self.image = pygame.transform.scale(ICON, (80, 120))
          self.screen.blit(icon, (half_screen_width - 50, half_screen_height - 250))
          reset = self.image = pygame.transform.scale(RESET, (80, 120))
          self.screen.blit(reset, (half_screen_width - 50 , half_screen_height - 120))
          self.menu.update_message(self.screen, 'Game over. Press any key to restart')
          self.menu.update_message(self.screen, f'Your score {self.score}', 30)
          self.menu.update_message(self.screen, f'highest score {self.highest_score}', 60)
          self.menu.update_message(self.screen, f'total deaths {self.death_count}', 90)
          self.menu.draw(self.screen)
        

        self.menu.update(self)
        
    def update_score(self):
        self.score += 1
    
    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self. score}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show  = round((self.player.power_time_up - pygame.time.get_ticks())/100, 2)
            if time_to_show >= 0:
                message = f'{self.player.power_up_type.capitalize()} is enable for {time_to_show} second'
                self.menu.update_message(self.screen, message, 0, (255,255,255))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
