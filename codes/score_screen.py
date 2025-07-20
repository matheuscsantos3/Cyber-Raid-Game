import pygame
import os
import sys
from codes.database import get_top_scores

<<<<<<< HEAD
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
=======
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
>>>>>>> 958f78a (Code and executable updated)

class ScoreScreen:
    def __init__(self, screen, final_time, final_score):
        self.screen = screen
        self.final_time = final_time
        self.final_score = final_score
<<<<<<< HEAD
        self.title_font = pygame.font.Font(os.path.join(BASE_DIR, "..", "assets", "fonts", "cyberpunk.ttf"), 72)
        self.neuropol_font = pygame.font.Font(os.path.join(BASE_DIR, "..", "assets", "fonts", "Neuropol X Rg.otf"), 28)
        self.text_font = pygame.font.Font(os.path.join(BASE_DIR, "..", "assets", "fonts", "cyberpunk.ttf"), 28)
        self.background = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "backgrounds", "menu_background.jpg")).convert()

        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(BASE_DIR, "..", "assets", "sounds", "menu_theme.ogg"))
=======
        self.title_font = pygame.font.Font(resource_path("assets/fonts/Cyberpunk.ttf"), 72)
        self.neuropol_font = pygame.font.Font(resource_path("assets/fonts/Neuropol X Rg.otf"), 28)
        self.text_font = pygame.font.Font(resource_path("assets/fonts/Cyberpunk.ttf"), 28)
        self.background = pygame.image.load(resource_path("assets/backgrounds/menu_background.jpg")).convert()

        pygame.mixer.init()
        pygame.mixer.music.load(resource_path("assets/sounds/menu_theme.ogg"))
>>>>>>> 958f78a (Code and executable updated)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.top_scores = get_top_scores()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        title_surface = self.title_font.render("SCORE", True, (255, 20, 147))
        title_rect = title_surface.get_rect(center=(400, 100))
        self.screen.blit(title_surface, title_rect)

        time_surface = self.neuropol_font.render(f"Time: {self.final_time:.2f}s", True, (0, 255, 255))
        time_rect = time_surface.get_rect(center=(400, 180))
        self.screen.blit(time_surface, time_rect)

        score_surface = self.neuropol_font.render(f"Score: {self.final_score}", True, (0, 255, 255))
        score_rect = score_surface.get_rect(center=(400, 220))
        self.screen.blit(score_surface, score_rect)

        ranking_title = self.neuropol_font.render("Top 5 Rankings", True, (255, 255, 0))
        ranking_rect = ranking_title.get_rect(center=(400, 280))
        self.screen.blit(ranking_title, ranking_rect)

        for i, (score, time) in enumerate(self.top_scores):
            rank_text = self.neuropol_font.render(f"{i+1}. Score: {score} | Time: {time:.2f}s", True, (0, 255, 255))
            self.screen.blit(rank_text, (220, 320 + i * 30))

        return_surface = self.text_font.render("Press ENTER to return to game", True, (0, 255, 255))
        return_rect = return_surface.get_rect(center=(400, 500))
        self.screen.blit(return_surface, return_rect)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return "menu"
        return "score"
