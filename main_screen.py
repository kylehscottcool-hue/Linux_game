import pygame
import level_1
import level_2

def main_menu():
    pygame.init()

    # Screen dimensions
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Main Menu")

    # Colors
    WHITE = ('#ADF5FF')
    BLACK = ('#13293D')
    GRAY = ('#8F9491')
    GREEN = ('#519872')
    BLUE = ('#1B98E0')
    RED = ('#D55672')
    YELLOW = ('#247BA0')
    PURPLE = ('#13293D')

    # Font
    font = pygame.font.Font(None, 50)

    # Buttons
    level_1_button = pygame.Rect(220, 150, 200, 50)
    level_2_button = pygame.Rect(220, 250, 200, 50)
    quit_button = pygame.Rect(220, 350, 200, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level_1_button.collidepoint(event.pos):
                    if level_1.run_level_1(screen):
                        level_2.run_level_2(screen)
                if level_2_button.collidepoint(event.pos):
                    level_2.run_level_2(screen)
                if quit_button.collidepoint(event.pos):
                    running = False

        # Drawing
        screen.fill(BLUE)

        pygame.draw.rect(screen, WHITE, level_1_button)
        pygame.draw.rect(screen, WHITE, level_2_button)
        pygame.draw.rect(screen, WHITE, quit_button)

        level_1_text = font.render("Level 1", True, BLACK)
        level_2_text = font.render("Level 2", True, BLACK)
        quit_button_text = font.render("  QUIT", True, BLACK)

        screen.blit(level_1_text, (level_1_button.x + 40, level_1_button.y + 10))
        screen.blit(level_2_text, (level_2_button.x + 40, level_2_button.y + 10))
        screen.blit(quit_button_text, (quit_button.x + 40, quit_button.y + 10))


        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main_menu()
