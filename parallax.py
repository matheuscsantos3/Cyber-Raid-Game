import pygame
import os

class ParallaxBackground:
    def __init__(self, screen, folder_path="assets/backgrounds/parallax", speed=1):
        self.screen = screen
        self.layers = []
        self.speeds = []

        layer_files = sorted(os.listdir(folder_path))
        for i, filename in enumerate(layer_files):
            if filename.endswith(".png"):
                image = pygame.image.load(os.path.join(folder_path, filename)).convert_alpha()
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
