import random
from game.components.meteorite.meteorite import Meteorite
from game.utils.constants import SCREEN_HEIGHT

class MeteoriteManager:

    def __init__(self):
        self.meteorites = []

    def update(self, game):
        self.add_meteorite()
        for meteorite in self.meteorites:
            meteorite.update(game)
            if meteorite.rect.y >= SCREEN_HEIGHT:
                self.meteorites.remove(meteorite)

    def draw(self, screen):
        for meteorite in self.meteorites:
            meteorite.draw(screen)

    def add_meteorite(self):  
        if len(self.meteorites) < 2:
            meteorite = Meteorite()
            self.meteorites.append(meteorite) 

    def reset(self):
        self.meteorites = [] 