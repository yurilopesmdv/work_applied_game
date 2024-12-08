import pygame
from DbManager import DBManager

class ScoreScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.running = True

    def run(self):
        db = DBManager()
        scores = db.get_top_scores()
        db.close()
        
        self.running = True

        menu_background = pygame.image.load('./assets/menu_background.jpg')
        menu_background = pygame.transform.scale(menu_background, (self.screen.get_width(), self.screen.get_height()))

        while self.running:
            self.screen.blit(menu_background, (0, 0))

            title = self.font.render("Melhores Pontuações", True, (255, 255, 255))
            self.screen.blit(title, (250, 50))

            for i, (nome, pontuacao) in enumerate(scores):
                text = self.font.render(f"{i + 1}. {nome} - {pontuacao}", True, (255, 255, 255))
                self.screen.blit(text, (200, 100 + i * 40))

            back_button = pygame.Rect(self.screen.get_width() // 2 - 150, self.screen.get_height() - 150, 300, 70)
            pygame.draw.rect(self.screen, (169, 169, 169), back_button)  # Cor cinza claro

            back_button_text = self.font.render("Voltar ao Menu", True, (0, 0, 0))  # Texto do botão em preto
            text_x = back_button.x + (back_button.width - back_button_text.get_width()) // 2
            text_y = back_button.y + (back_button.height - back_button_text.get_height()) // 2
            self.screen.blit(back_button_text, (text_x, text_y))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(event.pos):
                    self.running = False
                    return "menu"