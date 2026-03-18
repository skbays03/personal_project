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



class BottomLine(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))

    def draw(self, screen):

        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*4)

    def update(self, dt):
        pass



class LeftLine(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))

    def draw(self, screen):

        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*4)

    def update(self, dt):
        pass



class RightLine(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))

    def draw(self, screen):

        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*4)

    def update(self, dt):
        pass