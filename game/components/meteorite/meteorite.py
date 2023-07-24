import random
import pygame
from pygame.sprite import Sprite

from game.utils.constants import METEORITE, SCREEN_WIDTH

class Meteorite(Sprite):
    METEORITE_WIDTH = 40
    METEORITE_HEIGHT = 60
    Y_POS = 0
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050]
    SPEED_Y = 9
    SPEED_X = 10
    SPEED_X_DIAGONAL = 7  
    MOV_X = {0: 'left', 1: 'right'}
    METEORITE_IMAGEN = [METEORITE]

    def __init__(self):
        self.image = pygame.transform.scale(random.choice(self.METEORITE_IMAGEN), (self.METEORITE_WIDTH, self.METEORITE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 20)]
        self.rect.y = self.Y_POS
        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X
        self.speed_x_diagonal = self.SPEED_X_DIAGONAL
        self.movement_x = 'left'  
        self.move_x_for = random.randint(30, 50)
        self.index = 0

    def update(self, game):
        self.rect.y += self.speed_y
        self.rect.x -= self.speed_x 
        self.rect.x -= self.speed_x_diagonal  
        self.change_movement()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement(self):
        self.index += 1
        if self.index >= self.move_x_for or self.rect.left <= 0:
            self.movement_x = 'left'
            self.move_x_for = random.randint(30, 50)
            self.index = 0