import pygame
import time
import random
import os
import sys
from codes.parallax import ParallaxBackground
from codes.explosion import Explosion
from codes.database import save_score

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

class Enemy2:
    def __init__(self, x, y):
        self.frames = [
<<<<<<< HEAD
            pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "enemies", "level2", "enemy2_1.png")).convert_alpha(),
            pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "enemies", "level2", "enemy2_2.png")).convert_alpha()
=======
            pygame.image.load(resource_path("assets/enemies/level2/enemy2_1.png")).convert_alpha(),
            pygame.image.load(resource_path("assets/enemies/level2/enemy2_2.png")).convert_alpha()
>>>>>>> 958f78a (Code and executable updated)
        ]
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 10
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 2

    def update(self):
        self.rect.x -= self.speed
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.animation_timer = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def off_screen(self, screen_width):
        return self.rect.right < 0

class Player:
    def __init__(self, x, y):
<<<<<<< HEAD
        self.image = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "player", "player.png")).convert_alpha()
=======
        self.image = pygame.image.load(resource_path("assets/player/player.png")).convert_alpha()
>>>>>>> 958f78a (Code and executable updated)
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

def run_level2(screen, total_time_so_far=0, total_score_so_far=0):
    clock = pygame.time.Clock()
<<<<<<< HEAD
    font = pygame.font.Font(os.path.join(BASE_DIR, "..", "assets", "fonts", "Neuropol X Rg.otf"), 28)

    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(BASE_DIR, "..", "assets", "sounds", "level2.ogg"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    shoot_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "..", "assets", "sounds", "shoot.ogg"))
    shoot_sound.set_volume(0.1)

    explosion_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "..", "assets", "sounds", "explosion.ogg"))
=======
    font = pygame.font.Font(resource_path("assets/fonts/Neuropol X Rg.otf"), 28)

    pygame.mixer.init()
    pygame.mixer.music.load(resource_path("assets/sounds/level2.ogg"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    shoot_sound = pygame.mixer.Sound(resource_path("assets/sounds/shoot.ogg"))
    shoot_sound.set_volume(0.1)

    explosion_sound = pygame.mixer.Sound(resource_path("assets/sounds/explosion.ogg"))
>>>>>>> 958f78a (Code and executable updated)
    explosion_sound.set_volume(0.3)

    player = Player(100, screen.get_height() // 2)
    background = ParallaxBackground(screen, "assets/backgrounds/level2")
    bullets = []
    enemies = []
    explosions = []

    spawn_timer = 0
    spawn_interval = 120
    start_time = time.time()
    score = 0

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                return "menu"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.rect.right, player.rect.centery))
                shoot_sound.play()

        background.update()
        background.draw()

        keys = pygame.key.get_pressed()
        player.move(keys, screen.get_width(), screen.get_height())
        player.draw(screen)

        for bullet in bullets:
            bullet.update()
            bullet.draw(screen)
        bullets = [b for b in bullets if not b.off_screen(screen.get_width())]

        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            spawn_timer = 0
            y = random.randint(0, screen.get_height())
            enemies.append(Enemy2(screen.get_width() + 40, y))

        for enemy in enemies:
            enemy.update()
            enemy.draw(screen)
        enemies = [e for e in enemies if not e.off_screen(screen.get_width())]

        for enemy in enemies[:]:
            for bullet in bullets[:]:
                if bullet.rect.colliderect(enemy.rect.inflate(-10, -10)):
                    explosions.append(Explosion(enemy.rect.centerx, enemy.rect.centery))
                    explosion_sound.play()
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    score += 1
                    break

        for enemy in enemies:
            if player.rect.colliderect(enemy.rect.inflate(-40, -40)):
                explosions.append(Explosion(player.rect.centerx, player.rect.centery))
                pygame.mixer.music.stop()

<<<<<<< HEAD
                game_over_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "..", "assets", "sounds", "game_over.ogg"))
                game_over_sound.set_volume(0.8)
                game_over_sound.play()

                game_over_font = pygame.font.Font(os.path.join(BASE_DIR, "..", "assets", "fonts", "cyberpunk.ttf"), 72)
=======
                game_over_sound = pygame.mixer.Sound(resource_path("assets/sounds/game_over.ogg"))
                game_over_sound.set_volume(0.8)
                game_over_sound.play()

                game_over_font = pygame.font.Font(resource_path("assets/fonts/cyberpunk.ttf"), 72)
>>>>>>> 958f78a (Code and executable updated)
                game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
                game_over_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

                game_over = True
                while game_over:
                    clock.tick(60)
                    screen.fill((0, 0, 0))

                    for e in explosions:
                        e.update()
                        e.draw(screen)

                    screen.blit(game_over_text, game_over_rect)
                    pygame.display.flip()

                    if all(e.done for e in explosions):
                        pygame.time.delay(3000)
                        game_over = False

                return "menu"

        for e in explosions:
            e.update()
            e.draw(screen)
        explosions = [e for e in explosions if not e.done]

        elapsed = int(time.time() - start_time)
        timer = font.render(f"Time: {elapsed}s", True, (255, 255, 255))
        screen.blit(timer, (10, 10))

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (200, 10))

        pygame.display.flip()

        if elapsed >= 60:
            pygame.mixer.music.stop()
<<<<<<< HEAD
            pygame.mixer.Sound(os.path.join(BASE_DIR, "..", "assets", "sounds", "level_up.ogg")).play()
=======
            pygame.mixer.Sound(resource_path("assets/sounds/level_up.ogg")).play()
>>>>>>> 958f78a (Code and executable updated)
            pygame.time.delay(2000)
            final_time = total_time_so_far + elapsed
            final_score = total_score_so_far + score
            save_score(final_time, final_score)
            return "score", elapsed, score
