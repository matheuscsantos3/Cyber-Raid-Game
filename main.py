import pygame
import sys
from menu import Menu
from level1 import run_level1
from level2 import run_level2

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cyber Raid")
clock = pygame.time.Clock()

current_state = "menu"
menu = Menu(screen)

def main():
    global current_state
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_state == "menu":
            current_state = menu.handle_input()
            menu.draw()

        elif current_state == "game":
            phase1_result = run_level1(screen)
            if phase1_result == "next":
                phase2_result = run_level2(screen)
                if phase2_result == "menu":
                    current_state = "menu"
            else:
                current_state = "menu"

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
