import pygame
from constants import *
from lineshape import LineShape

class TopLine(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    def draw(self, screen):

        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*2)

    def update(self, dt):
        pass

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

class BottomLine(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    def draw(self, screen):

        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*2)

    def update(self, dt):
        pass

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

class LeftLine(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    def draw(self, screen):

        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*2)

    def update(self, dt):
        pass

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

class RightLine(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    def draw(self, screen):

        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*2)

    def update(self, dt):
        pass

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2