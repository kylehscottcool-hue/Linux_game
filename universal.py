# This is for varibales that will be used accross all of the levels and screens
# Indent means it is meant to go inside of the main game loop

# imports
import pygame
import universal
import main_screen

# Colors
WHITE = ('#ADF5FF')
BLACK = ('#13293D')
GRAY = ('#8F9491')
GREEN = ('#104911')
BLUE = ('#1B98E0')
RED = ('#D55672')
YELLOW = ('#FFD449')
PURPLE = ('#13293D')

# Player properties
player_width, player_height = 50, 50
player_x = 100
player_y = screen_height - player_height - border_thickness
player_speed = 5
player_vel_y = 0
onground = False
player_color = RED

# Force variables
gravity = 0.5
jump_power = -5


# Border
border_thickness = 5
border_color = GRAY

# Font
font = pygame.font.Font(None, 20)
level_font = pygame.font.Font(None, 50)

# Menu Button
menu_width, menu_height = 50, 30
menu_x = screen_width - border_thickness - menu_width
menu_y = border_thickness
menu_color = WHITE


# Input detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_button.collidepoint(event.pos):
                main_screen.main_menu()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player_x += player_speed
        if keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_w] and onground:
            player_vel_y = jump_power
            onground = False
        if keys[pygame.K_s]:
            player_y += player_speed
        if keys[pygame.K_ESCAPE]:
            running = False
        
# Apply gravity
    player_vel_y += gravity
    player_y += player_vel_y

# Stay within borders
    player_x = max(border_thickness, min(player_x, screen_width - player_width - border_thickness))
    if player_y > screen_height - player_height - border_thickness:
        player_y = screen_height - player_height - border_thickness
        player_vel_y = 0
        onground = True
    if player_y < border_thickness:
        player_y = border_thickness
        player_vel_y = 0
        onground = False

# Rects
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    platform_rect = pygame.Rect(platform_x, platform_y, platform_width, platform_height)
    portal_rect = pygame.Rect(portal_x, portal_y, portal_width, portal_height)
    menu_button = pygame.Rect(menu_x, menu_y, menu_width, menu_height)
    level_rect = pygame.Rect(screen_width // 2 - 100, border_thickness, 100, 100)

# Text
    menu_button_text = font.render("MENU", True, BLACK)
# Change "LEVEL 1" to whatever this level is for the next line
#    level_text = level_font.render("LEVEL 1", True, BLACK)

# Drawing
    screen.fill(BLUE)
# Draw border
    pygame.draw.rect(screen, GRAY, (0, 0, screen_width, screen_height), border_thickness)
# Draw platform
    pygame.draw.rect(screen, platform_color, (platform_x, platform_y, platform_width, platform_height))
# Draw portal
    pygame.draw.rect(screen, portal_color, (portal_x, portal_y, portal_width, portal_height))
# Draw player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
# Draw menu button
    pygame.draw.rect(screen, menu_color, menu_button)
    screen.blit(menu_button_text, (menu_button.x + 5, menu_button.y + 7))
# Draw level Text
    screen.blit(level_text, (level_rect.x + 40, level_rect.y + 10))

# Quiting
    pygame.display.flip()
    clock.tick(60)

