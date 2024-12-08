import pygame

class Background:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./assets/background.png')
        self.y1 = 0
        self.y2 = -self.screen.get_height()

    def update(self):
        self.y1 += 2
        self.y2 += 2

        if self.y1 > self.screen.get_height():
            self.y1 = self.y2 - self.screen.get_height()

        if self.y2 > self.screen.get_height():
            self.y2 = self.y1 - self.screen.get_height()

    def draw(self):
        self.screen.blit(self.image, (0, self.y1))
        self.screen.blit(self.image, (0, self.y2))
