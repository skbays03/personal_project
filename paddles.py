import pygame
from constants import *
from lineshape import LineShape

class PlayerPaddle(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))
        self.center = self.rect.center
    
    def move(self, dt):
        self.y1 += dt * 500
        self.y2 += dt * 500
        self.rect.y = min(self.y1, self.y2)
    
    def draw(self, screen):
        
        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*4)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.move(-dt)
        if keys[pygame.K_DOWN]:
            self.move(dt)

        current_screen_height = pygame.display.get_surface().get_height()
        min_y = 0 + LINE_WIDTH
        max_y = current_screen_height - LINE_WIDTH

        # Clamp the top of the paddle
        if self.y1 < min_y:
            self.y1 = min_y
            self.y2 = self.y1 + PADDLE_HEIGHT
            
        # Clamp the bottom of the paddle
        if self.y2 > max_y:
            self.y2 = max_y
            self.y1 = self.y2 - PADDLE_HEIGHT

        self.resize(self.x1, self.y1, self.x2, self.y2)

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.points = [x1, y1, x2, y2]
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))
        self.center = self.rect.center
        #print(self.center)
        #print(self.points)



class AIPaddle(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))
        self.center = self.rect.center
    
    def draw(self, screen):
        
        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*4)

    def update(self, dt):
        
        #movement logic for the AI paddle will go here, for now it just stays in the middle of the screen

        #Clamps the AI paddle to the confines of the screen
        current_screen_height = pygame.display.get_surface().get_height()
        min_y = 0 + LINE_WIDTH
        max_y = current_screen_height - LINE_WIDTH

        # Clamp the top of the paddle
        if self.y1 < min_y:
            self.y1 = min_y
            self.y2 = self.y1 + PADDLE_HEIGHT
            
        # Clamp the bottom of the paddle
        if self.y2 > max_y:
            self.y2 = max_y
            self.y1 = self.y2 - PADDLE_HEIGHT

        self.resize(self.x1, self.y1, self.x2, self.y2)

    def resize(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.points = [x1, y1, x2, y2]
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))
        self.center = self.rect.center
        #print(self.center)
        #print(self.points)