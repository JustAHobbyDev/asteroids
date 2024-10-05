import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        # self.position = pygame.math.Vector2(x, y)
        self.velocity = 150.0
        # self.radius = SHOT_RADIUS

        
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

        
    def update(self, dt):
        self.position += self.velocity * dt