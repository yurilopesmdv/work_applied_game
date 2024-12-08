import pygame
import time
import random
from Player import Player
from Obstacle import Obstacle
from Background import Background
from DbManager import DBManager
from InputName import InputName

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.player_score = 0
        self.player_name = ""
        
        self.player = Player(self.screen)
        self.background = Background(self.screen)
        self.obstacles = []
        self.spawn_rate = 1 
        self.obstacle_speed = 5
        self.last_spawn_time = time.time()
    
    def reset_game(self):
        """Método para reiniciar o jogo, resetando todas as variáveis importantes."""
        self.player_score = 0
        self.player_name = ""
        self.player = Player(self.screen)
        self.background = Background(self.screen)
        self.obstacles.clear()
        self.spawn_rate = 1 
        self.obstacle_speed = 5
        self.last_spawn_time = time.time()

    def run(self):
        input_name = InputName(self.screen)
        self.player_name = input_name.run()
        self.running = True

        while self.running:
            self.screen.fill((0, 0, 0))
            self.handle_events()

            if self.running:
                self.background.update()
                self.background.draw()

                self.player.update()
                self.player.draw()

                self.spawn_obstacles()

                for obstacle in self.obstacles:
                    obstacle.update()
                    obstacle.draw()

                if self.check_collision():
                    self.end_game()

                self.player_score += 1

                score_text = pygame.font.Font(None, 50).render(f"Pontos: {self.player_score}", True, (255, 255, 255))
                self.screen.blit(score_text, (10, 10))

                if self.player_score % 100 == 0 and self.player_score > 0:
                    self.obstacle_speed += 1

                if self.player_score % 50 == 0 and self.player_score > 0:
                    self.spawn_rate = max(0.5, self.spawn_rate - 0.1)

            pygame.display.update()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def check_collision(self):
        for obstacle in self.obstacles:
            if self.player.rect.colliderect(obstacle.rect):
                return True
        return False

    def spawn_obstacles(self):
        if time.time() - self.last_spawn_time >= self.spawn_rate:
            for _ in range(random.randint(1, 2)):
                obstacle = Obstacle(self.screen, self.obstacle_speed)
                self.obstacles.append(obstacle)

            self.last_spawn_time = time.time()

    def end_game(self):
        db = DBManager()
        db.insert_score(self.player_name, self.player_score)
        db.close()

        self.show_game_over_screen()

    def show_game_over_screen(self):
        game_over_font = pygame.font.Font(None, 80)
        score_font = pygame.font.Font(None, 50)

        background = pygame.image.load('./assets/background.png')
        background = pygame.transform.scale(background, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(background, (0, 0))

        game_over_text = game_over_font.render("GAME OVER", True, (0, 0, 0))
        score_text = score_font.render(f"Score: {self.player_score}", True, (0, 0, 0))

        self.screen.blit(game_over_text, (self.screen.get_width() // 2 - game_over_text.get_width() // 2, 100))
        self.screen.blit(score_text, (self.screen.get_width() // 2 - score_text.get_width() // 2, 200))

        back_button = pygame.Rect(self.screen.get_width() // 2 - 150, 300, 300, 70)
    
        pygame.draw.rect(self.screen, (169, 169, 169), back_button)

        back_button_text = score_font.render("Ver pontuações", True, (0, 0, 0))

        text_x = back_button.x + (back_button.width - back_button_text.get_width()) // 2
        text_y = back_button.y + (back_button.height - back_button_text.get_height()) // 2
        self.screen.blit(back_button_text, (text_x, text_y))

        pygame.display.update()

        waiting_for_click = True
        while waiting_for_click:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        waiting_for_click = False 
                        self.running = False