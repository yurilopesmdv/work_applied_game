import pygame
import random

class Obstacle:
    def __init__(self, screen, speed):
        self.screen = screen
        self.image = pygame.image.load('./assets/obstacle.png') 
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width) 
        self.rect.y = -self.rect.height
        self.speed = speed 

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen.get_height():
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)

    def draw(self):
        self.screen.blit(self.image, self.rect)
