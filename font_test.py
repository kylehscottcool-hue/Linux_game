
import pygame

pygame.init()

try:
    font = pygame.font.Font(None, 50)
    print("Font loaded successfully!")
except Exception as e:
    print(f"Error loading font: {e}")

pygame.quit()
