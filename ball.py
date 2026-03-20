import pygame
from constants import *
from circleshape import *

class Ball(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.velocity = pygame.Vector2(random.choice([-10, 10]), random.choice([-10, 10])).normalize() * 400

    def draw(self, screen):
        pygame.draw.circle(screen, "black", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)