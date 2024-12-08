import pygame

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (300, 500)
        self.speed = 6

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()

    def draw(self):
        self.screen.blit(self.image, self.rect)
