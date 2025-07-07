import pygame
import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font(os.path.join(BASE_DIR, "..", "assets", "fonts", "cyberpunk.ttf"), 72)
        self.option_font = pygame.font.Font(os.path.join(BASE_DIR, "..", "assets", "fonts", "cyberpunk.ttf"), 28)
        self.background = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "backgrounds", "menu_background.jpg")).convert()

        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(BASE_DIR, "..", "assets", "sounds", "menu_theme.ogg"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        title_surface = self.title_font.render("CYBER RAID", True, (255, 20, 147))
        title_rect = title_surface.get_rect(center=(400, 160))
        self.screen.blit(title_surface, title_rect)
        start_surface = self.option_font.render("Press ENTER to start", True, (0, 255, 255))
        start_rect = start_surface.get_rect(center=(400, 260))
        self.screen.blit(start_surface, start_rect)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return "game"
        return "menu"
