import pygame
from Menu import Menu
from Game import Game
from Score import ScoreScreen

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Runner")

def main():
    menu_screen = Menu(screen)
    game_screen = Game(screen)
    score_screen = ScoreScreen(screen)

    current_screen = "menu"

    while True:
        if current_screen == "menu":
            choice = menu_screen.run()
            if choice == "start":
                current_screen = "game"
            elif choice == "score":
                current_screen = "score"
            elif choice == "exit":
                break
        elif current_screen == "game":
            game_screen.reset_game()
            game_screen.run()
            current_screen = "menu"
        elif current_screen == "score":
            result = score_screen.run()
            if result == "menu":
                current_screen = "menu"
            elif result == "exit":
                break

    pygame.quit()

if __name__ == "__main__":
    main()