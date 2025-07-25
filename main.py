import pygame
import sys
import os
from codes.menu import Menu
from codes.level1 import run_level1
from codes.level2 import run_level2
from codes.score_screen import ScoreScreen 

from codes.database import initialize_db

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Cyber Raid")
    clock = pygame.time.Clock()

    current_state = "menu"
    menu = Menu(screen)
    score_screen = None

    initialize_db()
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
            if isinstance(phase1_result, tuple) and phase1_result[0] == "next":
                phase1_time = phase1_result[1]
                phase1_score = phase1_result[2]

                phase2_result = run_level2(screen, phase1_time, phase1_score)
                if isinstance(phase2_result, tuple) and phase2_result[0] == "score":
                    total_time = phase1_time + phase2_result[1]
                    total_score = phase1_score + phase2_result[2]
                    score_screen = ScoreScreen(screen, total_time, total_score)
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
