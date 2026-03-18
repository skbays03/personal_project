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
        self.rect = pygame.Rect(
        min(x1, x2), 
        min(y1, y2) - (buffer // 2), # Offset to center the thickness
        max(abs(x2 - x1), buffer), 
        buffer
        )   

    def collides_with(self, other):
        # 1. Create a real 'Area' for this line (e.g., the TopLine)
        # We add a small 'buffer' (like 5 pixels) so the line isn't infinitely thin
        self_rect = pygame.Rect(
            min(self.x1, self.x2), 
            min(self.y1, self.y2), 
            max(abs(self.x2 - self.x1), 5), # Ensure at least 5px width
            max(abs(self.y2 - self.y1), 5)  # Ensure at least 5px height
        )
        
        # 2. Create a real 'Area' for the player/other object
        other_rect = pygame.Rect(
            min(other.x1, other.x2), 
            min(other.y1, other.y2), 
            max(abs(other.x2 - other.x1), 5), 
            max(abs(other.y2 - other.y1), 5)
        )
        
        # 3. Use Pygame's optimized area collision
        return self_rect.colliderect(other_rect)