import pygame
from constants import *
from lineshape import LineShape

class PlayerPaddle(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))
        self.center = self.rect.center
        self.score = 0
        self.current_screen_height = pygame.display.get_surface().get_height()
        self.current_screen_width = pygame.display.get_surface().get_width()
    
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
        self.current_screen_height = pygame.display.get_surface().get_height()
        self.current_screen_width = pygame.display.get_surface().get_width()
        self.score_board(pygame.display.get_surface())

    def score_board(self, screen):
        font = pygame.font.SysFont(None, 50)
        score_surface = font.render(f"{self.score}", True, "black")
        screen.blit(score_surface, (self.current_screen_width//2 - 150, 20))



class AIPaddle(LineShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2-x1), abs(y2-y1))
        self.center = self.rect.center
        self.score = 0
        self.current_screen_height = pygame.display.get_surface().get_height()
        self.current_screen_width = pygame.display.get_surface().get_width()

    def move(self, dt):
        self.y1 += dt * 500
        self.y2 += dt * 500
        self.rect.y = min(self.y1, self.y2)
    
    def draw(self, screen):
        
        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), LINE_WIDTH*4)

    def update(self, dt, ball):
        
            # 1. Prediction Logic
        if ball.velocity.x > 0:
            # Move toward predicted path
            target = ball.position.y
        else:
            # Idle at center
            target = pygame.display.get_surface().get_height() // 2
        
        # 2. Movement with a "Dead Zone" to prevent shaking
        if abs(self.center[1] - target) > 5:
            direction = 1 if target > self.center[1] else -1
            # AI moves at 25% of standard speed to be beatable
            self.move(direction * dt * 0.25)

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
        self.current_screen_height = pygame.display.get_surface().get_height()
        self.current_screen_width = pygame.display.get_surface().get_width()
        self.score_board(pygame.display.get_surface())

    def score_board(self, screen):
        font = pygame.font.SysFont(None, 50)
        score_surface = font.render(f"{self.score}", True, "black")
        screen.blit(score_surface, (self.current_screen_width//2 + 150, 20))