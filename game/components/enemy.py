import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet

from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3, SCREEN_WIDTH

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    Y_POS = 20
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050]
    SPEED_Y = 6
    SPEED_X = 8
    MOV_X = {0: 'left', 1: 'right'}

    ENEMY_IMAGEN = [ENEMY_1, ENEMY_2, ENEMY_3]
    
    def __init__(self, enemy_type):
        self.image = pygame.transform.scale(random.choice(self.ENEMY_IMAGEN), (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 20)]
        self.rect.y = self.Y_POS
        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 50)
        self.index = 0
        self.type = 'enemy' 
        self.enemy_type = enemy_type
        self._speeds = {
            1: {"speed_x": 1, "speed_y": 4},
            2: {"speed_x": 9, "speed_y": 2},
            3: {"speed_x": 3, "speed_y": 4},
        }
        self.speed_x = self._speeds[enemy_type]["speed_x"]
        self.speed_y = self._speeds[enemy_type]["speed_y"]
        self.shooting_time =  random.randint(30, 50)
        
        self.set_speeds()
        
    def set_speeds(self):
        if self.enemy_type == 1:
            self.speed_x = 3
            self.speed_y = 3
        elif self.enemy_type == 2:
            self.speed_x = 9
            self.speed_y = 2
        elif self.enemy_type == 3:
            self.speed_x = 1
            self.speed_y = 5

    def update(self, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        self.change_movement()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement(self):
        self.index += 1
        if self.index >= self.move_x_for or self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            if self.movement_x == 'right':
                self.movement_x = 'left'
            elif self.movement_x == 'left':
                self.movement_x = 'right'
            self.move_x_for
            self.index = 0

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)