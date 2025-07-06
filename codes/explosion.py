import pygame

class Explosion:
    def __init__(self, x, y):
        self.frames = [
            pygame.image.load(f"assets/effects/playerExplosion{i}.png").convert_alpha()
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
