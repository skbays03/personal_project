import pygame
from constants import *

class LineShape(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.points = [x1, y1, x2, y2]
    
    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.points = [x1, y1, x2, y2]