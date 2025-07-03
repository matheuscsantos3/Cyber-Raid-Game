import pygame
import time
from parallax import ParallaxBackground

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/player/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = 5

    def move(self, keys, screen_width, screen_height):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Keep player inside screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((12, 4))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def off_screen(self, screen_width):
        return self.rect.left > screen_width


def run_level1():
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    font_path = "assets/fonts/Neuropol X Rg.otf"
    font = pygame.font.Font(font_path, 28)

    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/level1.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    player = Player(x=screen.get_width() // 2, y=screen.get_height() - 50)
    background = ParallaxBackground(screen, "assets/backgrounds/parallax")
    bullets = []

    start_time = time.time()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.right, player.rect.centery)
                    bullets.append(bullet)

        background.update()
        background.draw()

        keys = pygame.key.get_pressed()
        player.move(keys, screen.get_width(), screen.get_height())
        player.draw(screen)

        for bullet in bullets:
            bullet.update()
            bullet.draw(screen)

        bullets = [b for b in bullets if not b.off_screen(screen.get_width())]

        elapsed = int(time.time() - start_time)
        timer = font.render(f"Time: {elapsed}s", True, (255, 255, 255))
        screen.blit(timer, (10, 10))

        pygame.display.flip()

        if elapsed >= 60:
            pygame.mixer.music.stop()
            running = False
