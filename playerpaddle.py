import pygame
from constants import *
from lineshape import LineShape

class PlayerPaddle(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))
    
    def move(self, dt):
        self.y1 += dt * 500
        self.y2 += dt * 500
    
    def draw(self, screen):
        
        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*4)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.move(-dt)
        if keys[pygame.K_DOWN]:
            self.move(dt)

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.points = [x1, y1, x2, y2]
        # Update the internal rect for collisions
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))
        