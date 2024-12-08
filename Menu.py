import pygame
from Button import Button

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        self.font = pygame.font.Font(None, 60)

        self.background = pygame.image.load("assets/menu_background.jpg")
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

        self.buttons.append(Button("Iniciar Jogo", 300, 200, 200, 60, (200, 200, 200), (150, 150, 150), self.font))
        self.buttons.append(Button("Placar", 300, 300, 200, 60, (200, 200, 200), (150, 150, 150), self.font))
        self.buttons.append(Button("Sair", 300, 400, 200, 60, (200, 200, 200), (150, 150, 150), self.font))

    def run(self):
        while True:
            self.screen.blit(self.background, (0, 0))

            if self.buttons[0].draw(self.screen):
                return "start"
            if self.buttons[1].draw(self.screen):
                return "score"
            if self.buttons[2].draw(self.screen):
                return "exit"

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "exit"