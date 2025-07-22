import pygame
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class ParallaxBackground:
    def __init__(self, screen, folder_path=None, speed=1):
        self.screen = screen
        self.layers = []
        self.speeds = []

        if folder_path is None:
            folder_path = resource_path("assets/backgrounds/parallax")
        else:
            folder_path = resource_path(folder_path)

        layer_files = sorted(os.listdir(folder_path))
        for i, filename in enumerate(layer_files):
            if filename.endswith(".png"):
                image_path = os.path.join(folder_path, filename)
                image = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image, screen.get_size())
                self.layers.append([image, 0])
                self.speeds.append(speed * (i + 1) * 0.1)

    def update(self):
        for i, (image, x) in enumerate(self.layers):
            speed = self.speeds[i]
            x -= speed
            if x <= -self.screen.get_width():
                x = 0
            self.layers[i][1] = x

    def draw(self):
        for image, x in self.layers:
            self.screen.blit(image, (x, 0))
            self.screen.blit(image, (x + self.screen.get_width(), 0))
