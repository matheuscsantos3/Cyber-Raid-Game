import pygame

class ScoreScreen:
    def __init__(self, screen, final_time, final_score):
        self.screen = screen
        self.final_time = final_time
        self.final_score = final_score
        self.title_font = pygame.font.Font("assets/fonts/cyberpunk.ttf", 72)
        self.neuropol_font = pygame.font.Font("assets/fonts/Neuropol X Rg.otf", 28)
        self.text_font = pygame.font.Font("assets/fonts/cyberpunk.ttf", 28)
        self.background = pygame.image.load("assets/backgrounds/menu_background.jpg").convert()

        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/menu_theme.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        title_surface = self.title_font.render("SCORE", True, (255, 20, 147))
        title_rect = title_surface.get_rect(center=(400, 140))
        self.screen.blit(title_surface, title_rect)

        time_surface = self.neuropol_font.render(f"Time: {self.final_time:.2f}s", True, (0, 255, 255))
        time_rect = time_surface.get_rect(center=(400, 240))
        self.screen.blit(time_surface, time_rect)

        score_surface = self.neuropol_font.render(f"Score: {self.final_score}", True, (0, 255, 255))
        score_rect = score_surface.get_rect(center=(400, 290))
        self.screen.blit(score_surface, score_rect)

        return_surface = self.text_font.render("Press ENTER to return to game", True, (0, 255, 255))
        return_rect = return_surface.get_rect(center=(400, 380))
        self.screen.blit(return_surface, return_rect)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return "menu"
        return "score"

