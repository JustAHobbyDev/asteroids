import random
import pygame
import circleshape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.math.Vector2(x, y)

        
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

        
    def update(self, dt):
        print(f'position: {self.position}]\nvelocity: {self.velocity}')
        self.position = self.position + self.velocity * dt

        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        r = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(self.position.x, self.position.y, r)
        asteroid_a.velocity = a * 1.2
        asteroid_b = Asteroid(self.position.x, self.position.y, r)
        asteroid_b.velocity = b * 1.2