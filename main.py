import pygame

print('Setup Started')
pygame.init()
window = pygame.display.set_mode((800, 600))
print('Setup Finished')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

