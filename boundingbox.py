import pygame
from constants import *
from lineshape import LineShape

class TopLine(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))

    def draw(self, screen):

        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*4)

    def update(self, dt):
        pass

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.points = [x1, y1, x2, y2]
        # Update the internal rect for collisions
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))

class BottomLine(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))

    def draw(self, screen):

        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*4)

    def update(self, dt):
        pass

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.points = [x1, y1, x2, y2]
        # Update the internal rect for collisions
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))

class LeftLine(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))

    def draw(self, screen):

        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*4)

    def update(self, dt):
        pass

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.points = [x1, y1, x2, y2]
        # Update the internal rect for collisions
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))

class RightLine(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))

    def draw(self, screen):

        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*4)

    def update(self, dt):
        pass

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.points = [x1, y1, x2, y2]
        # Update the internal rect for collisions
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))