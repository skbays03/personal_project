import pygame
from rectshape import RectShape
from constants import *

class PauseMenu(RectShape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    # pausemenu.py

    def draw(self, screen):
        current_w = screen.get_width()
        current_h = screen.get_height()

        pygame.draw.rect(screen, "black", self.points, LINE_WIDTH*2)

        welcome_font = pygame.font.SysFont(None, 50)
        instruction_font = pygame.font.SysFont(None, 30)
        
        text_surface = welcome_font.render("Game Paused...", True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (current_w // 2, current_h // 2 - 25) # Replaced SCREEN_WIDTH/HEIGHT
        screen.blit(text_surface, text_rect)

        text_surface = instruction_font.render("Press enter to continue", True, "black")
        text_rect = text_surface.get_rect()
        text_rect.center = (current_w // 2, current_h // 2 + 25)
        screen.blit(text_surface, text_rect)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # Transition to the actual game when the user presses the enter key
        if keys[pygame.K_RETURN]:
            self.kill()