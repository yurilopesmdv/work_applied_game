import pygame

class InputName:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.input_box = pygame.Rect(200, 300, 400, 50)
        self.text = ''
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load('./assets/menu_background.jpg') 
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

    def run(self):
        running = True
        while running:
            self.screen.blit(self.background, (0, 0))

            title_text = self.font.render("Digite seu nome:", True, (255, 255, 255))
            self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, 100))

            txt_surface = self.font.render(self.text, True, self.color)
            width = max(400, txt_surface.get_width()+10)
            self.input_box.w = width
            self.screen.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
            pygame.draw.rect(self.screen, self.color, self.input_box, 2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(event.pos):
                        self.active = True
                    else:
                        self.active = False
                    self.color = self.color_active if self.active else self.color_inactive
                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            return self.text
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode

            pygame.display.update()
            self.clock.tick(30)