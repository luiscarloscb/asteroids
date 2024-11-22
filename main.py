import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Store the screen surface
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_loop(screen)  # Pass screen to game_loop

def game_loop(screen):
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill screen with red color
        screen.fill((233, 0, 0))  # Use the screen surface to fill
        pygame.display.flip()

    pygame.quit()  # Clean up pygame when done

if __name__ == "__main__":
    main()