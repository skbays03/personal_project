import pygame
from rectshape import RectShape
from constants import *

class MainMenu(RectShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    def draw(self, screen):
        # Draw border of the menu
        pygame.draw.rect(screen, "black", self.points, LINE_WIDTH*2)

        # Set font types and sizes
        welcome_font = pygame.font.SysFont(None, 50)
        instruction_font = pygame.font.SysFont(None, 30)
        
        # Render and position the welcome text
        text_surface = welcome_font.render("Welcome to Pong!", True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 25)
        screen.blit(text_surface, text_rect)

        # Render and position the instruction text
        text_surface = instruction_font.render("Press enter to continue", True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)
        screen.blit(text_surface, text_rect)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # Transition to the actual game when the user presses the enter key
        if keys[pygame.K_RETURN]:
            pass # TODO: transition to the actual game