import pygame
import sys
from menu import Menu
from level1 import run_level1
from level2 import run_level2
from score_screen import ScoreScreen

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cyber Raid")
clock = pygame.time.Clock()

current_state = "menu"
menu = Menu(screen)
score_screen = None

def main():
    global current_state, score_screen
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
                if isinstance(phase2_result, tuple) and phase2_result[0] == "score":
                    score_screen = ScoreScreen(screen, phase2_result[1], phase2_result[2])
                    current_state = "score"
                elif phase2_result == "menu":
                    current_state = "menu"
            else:
                current_state = "menu"

        elif current_state == "score":
            score_screen.draw()
            next_screen = score_screen.handle_input()
            if next_screen == "menu":
                current_state = "menu"

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
