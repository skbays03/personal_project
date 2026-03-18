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
        buffer = 5 
        width = max(abs(self.x2 - self.x1), buffer)
        height = max(abs(self.y2 - self.y1), buffer)
        self.rect = pygame.Rect(min(self.x1, self.x2), min(self.y1, self.y2), width, height)
    
    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        buffer = 5
        width = max(abs(self.x2 - self.x1), buffer)
        height = max(abs(self.y2 - self.y1), buffer)
        self.rect = pygame.Rect(min(self.x1, self.x2), min(self.y1, self.y2), width, height)

    def collides_with(self, other):
        if hasattr(other, 'rect'):
            return self.rect.colliderect(other.rect)
        return False