# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, drawable, updatable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    timer = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        screen.fill((0,0,0), rect=None, special_flags=0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                return False

        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)
        
        pygame.display.flip()
        dt = (timer.tick(60))/1000

        for asteroid in asteroids:
            if player.collides(asteroid):
                print("Game over!")
                sys.exit()

if __name__ == "__main__":
    main()
