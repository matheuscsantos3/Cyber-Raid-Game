import pygame

class Enemy:
    def __init__(self, x, y):
        self.frames = [
            pygame.image.load("assets/enemies/enemy.png").convert_alpha(),
            pygame.image.load("assets/enemies/enemyloop.png").convert_alpha()
        ]
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 10

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 2

    def update(self):
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.animation_timer = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def off_screen(self, screen_height):
        return self.rect.top > screen_height
