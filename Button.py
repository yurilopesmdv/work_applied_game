import pygame

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, font):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.font = font

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        is_hovered = self.rect.collidepoint(mouse)

        current_color = self.hover_color if is_hovered else self.color
        pygame.draw.rect(screen, current_color, self.rect)

        text_surface = self.font.render(self.text, True, (0, 0, 0))

        while text_surface.get_width() > self.rect.width - 10:
            font_size = self.font.size("A")[1] - 1
            self.font = pygame.font.Font(None, font_size)
            text_surface = self.font.render(self.text, True, (0, 0, 0))

        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        return click[0] and is_hovered