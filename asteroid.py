import pygame
import circleshape


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.math.Vector2(x, y)
        self.velocity = 150.0

        
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

        
    def update(self, dt):
        self.position += self.velocity * dt