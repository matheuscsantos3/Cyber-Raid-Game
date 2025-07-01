import pygame
import sys
from menu import Menu

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cyber Raid")
clock = pygame.time.Clock()

# Game state
current_state = "menu"

# Create menu
menu = Menu(screen)

def main():
    global current_state
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # State control
        if current_state == "menu":
            current_state = menu.handle_input()
            menu.draw()

        elif current_state == "game":
            screen.fill((0, 0, 0))  

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
