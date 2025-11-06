import pygame
import level_4
import main_screen

def run_level_5():
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Level 5")

    # Colors
    WHITE = ('#ADF5FF')
    BLACK = ('#13293D')
    GRAY = ('#8F9491')
    GREEN = ('#104911')
    BLUE = ('#1B98E0')
    RED = ('#D55672')
    YELLOW = ('#FFD449')
    PURPLE = ('#13293D')

    # Border
    border_thickness = 5
    border_color = GRAY

    # Font
    font = pygame.font.Font(None, 20)
    level_font = pygame.font.Font(None, 50)

    # Player properties
    player_width, player_height = 50, 50
    player_x = 100
    player_y = screen_height - player_height - border_thickness
    player_speed = 5
    player_vel_x = 0
    player_vel_y = 0
    onground = False
    player_color = RED

    # Slope properties
    



