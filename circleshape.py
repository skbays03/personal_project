import pygame
from constants import *
from paddles import *
from boundingbox import *

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def resize(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def collides_with(self, other):
        if isinstance(other, TopLine) or isinstance(other, BottomLine):
            return abs(self.position.y - other.y1) < self.radius
        elif isinstance(other, PlayerPaddle) or isinstance(other, AIPaddle):
            closest_x = max(other.x1, min(self.position.x, other.x2))
            closest_y = max(other.y1, min(self.position.y, other.y2))
            distance = pygame.Vector2(closest_x - self.position.x, closest_y - self.position.y).length()
            return distance < self.radius
        elif isinstance(other, LeftLine) or isinstance(other, RightLine):
            return abs(self.position.x - other.x1) < self.radius
        return False