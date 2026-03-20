import pygame
from constants import *
from circleshape import *
import random

class Ball(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.velocity = pygame.Vector2(random.choice([-10, 10]), random.choice([-10, 10])).normalize() * 400
        self.speed = 200
        self.acceleration = 20

    def draw(self, screen):
        pygame.draw.circle(screen, "black", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.velocity = self.velocity.normalize() * self.speed
        self.speed += self.acceleration * dt