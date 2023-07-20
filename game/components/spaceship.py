import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH

class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH//2) - SPACESHIP_WIDTH//2
    Y_POS = 500
    SPEED = 10

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
    def update(self, user_input):
     if user_input[pygame.K_LEFT]:
        self.rect.x -= self.SPEED
        if self.rect.left < 0:
           self.rect.left = SCREEN_WIDTH - self.SPACESHIP_WIDTH
     elif user_input[pygame.K_RIGHT]:
        self.rect.x += self.SPEED
        if self.rect.right > SCREEN_WIDTH:
           self.rect.right = self.SPACESHIP_WIDTH          
     elif user_input[pygame.K_UP]:
        if self.rect.top > SCREEN_HEIGHT//2:
            self.rect.y -= self.SPEED
     elif user_input[pygame.K_DOWN]:
        if self.rect.bottom < SCREEN_HEIGHT:
           self.rect.bottom += self.SPEED
       
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y)) 