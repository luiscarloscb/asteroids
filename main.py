import pygame
import sys
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Store the screen surface
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_loop(screen)  # Pass screen to game_loop

def game_loop(screen):
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    running = True
    clock = pygame.time.Clock()
    dt = 0
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill screen with red color
        screen.fill("black")  # Use the screen surface to fill
        for d in drawable:
            d.draw(screen)
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if a.collides(player):
                print("Game over!")
                sys.exit()
            for s in shots:
                if s.collides(a):
                    a.split()
                    s.kill()

        pygame.display.flip()
        dt = clock.tick(60)/1000

    pygame.quit()  # Clean up pygame when done

if __name__ == "__main__":
    main()
