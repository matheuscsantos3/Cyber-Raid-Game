import pygame
import os
import sys

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

class Explosion:
    def __init__(self, x, y):
        self.frames = [
<<<<<<< HEAD
            pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "effects", f"playerExplosion{i}.png")).convert_alpha()
=======
            pygame.image.load(resource_path(f"assets/effects/playerExplosion{i}.png")).convert_alpha()
>>>>>>> 958f78a (Code and executable updated)
            for i in range(1, 13)
        ]
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.done = False
        self.frame_rate = 3
        self.frame_count = 0

    def update(self):
        self.frame_count += 1
        if self.frame_count >= self.frame_rate:
            self.index += 1
            self.frame_count = 0
            if self.index >= len(self.frames):
                self.done = True
            else:
                self.image = self.frames[self.index]

    def draw(self, screen):
        if not self.done:
            screen.blit(self.image, self.rect)
