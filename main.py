import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x, y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))

        for entity in updatable:
            entity.update(dt)
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == '__main__':
    main()