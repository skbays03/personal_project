import pygame
from rectshape import RectShape
from constants import *
from main import main
import sys

class MainMenu(RectShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    def draw(self, screen):

        # Temp rect object for positioning
        menu_rect = pygame.Rect(self.points)

        # Draw border using the dynamic points
        pygame.draw.rect(screen, "black", self.points, LINE_WIDTH*2)

        # Set font types and sizes
        welcome_font = pygame.font.SysFont(None, 50)
        instruction_font = pygame.font.SysFont(None, 30)
        
        # Render and position the welcome text
        text_surface = welcome_font.render("Welcome to Pong!", True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (menu_rect.centerx, menu_rect.centery - 30)
        screen.blit(text_surface, text_rect)

        # Render and position instruction text
        text_surface = instruction_font.render("Press enter to continue", True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (menu_rect.centerx, menu_rect.centery + 30)
        screen.blit(text_surface, text_rect)

        text_surface = instruction_font.render("or ESC to exit", True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (menu_rect.centerx, menu_rect.centery + 60)
        screen.blit(text_surface, text_rect)

    def update(self, dt):
        
        keys = pygame.key.get_pressed()
        
        # Transition to the actual game when the user presses the enter key
        if keys[pygame.K_RETURN]:
            self.kill()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

class PauseMenu(RectShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    def draw(self, screen):

        # Temp rect object for positioning
        pause_rect = pygame.Rect(self.points)

        # Draw border using the dynamic points
        pygame.draw.rect(screen, "black", self.points, LINE_WIDTH*2)

        # Set font types and sizes
        welcome_font = pygame.font.SysFont(None, 50)
        instruction_font = pygame.font.SysFont(None, 30)
        
        # Render and position the welcome text
        text_surface = welcome_font.render("Game Paused...", True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (pause_rect.centerx, pause_rect.centery - 30)
        screen.blit(text_surface, text_rect)

        # Render and position instruction text
        text_surface = instruction_font.render("Press enter to continue", True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (pause_rect.centerx, pause_rect.centery + 30)
        screen.blit(text_surface, text_rect)

    def update(self, dt):

        keys = pygame.key.get_pressed()
        
        # Transition to the actual game when the user presses the enter key
        if keys[pygame.K_RETURN]:
            self.kill()

class WinConditionMenu(RectShape):
    def __init__(self, x1, y1, x2, y2, winner):
        super().__init__(x1, y1, x2, y2)
        self.winner = winner

    def draw(self, screen):

        # Temp rect object for positioning
        win_rect = pygame.Rect(self.points)

        # Draw border using the dynamic points
        pygame.draw.rect(screen, "black", self.points, LINE_WIDTH*2)

        # Set font types and sizes
        welcome_font = pygame.font.SysFont(None, 50)
        instruction_font = pygame.font.SysFont(None, 30)
        
        # Render and position the welcome text
        text_surface = welcome_font.render(f"{self.winner} wins!", True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (win_rect.centerx, win_rect.centery - 30)
        screen.blit(text_surface, text_rect)

        # Render and position instruction text
        text_surface = instruction_font.render("Press esc to exit", True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (win_rect.centerx, win_rect.centery + 30)
        screen.blit(text_surface, text_rect)

        text_surface = instruction_font.render("or enter to play again", True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (win_rect.centerx, win_rect.centery + 60)
        screen.blit(text_surface, text_rect)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # Transition to the actual game when the user presses the enter key
        if keys[pygame.K_ESCAPE]:
            sys.exit()