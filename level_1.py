import pygame
# import SysFont
import sys
pygame.init()

# Screen dimensions
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Help Me")

# Border thickness
border_thickness = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (160, 32, 240)

# Platform properties (unmovable rectangle)
platform_width = screen_width // 2
platform_height = 20
platform_x = screen_width - platform_width - border_thickness
platform_y = screen_height - platform_height - 100 - border_thickness
platform_color = GRAY

# Player properties
player_width, player_height = 50, 50
player_x = 100
player_y = screen_height - player_height - border_thickness
player_speed = 5
player_vel_y = 0
onground = False

# Force variables
gravity = 0.5
jump_power = -20

# Portal properties
portal_width = 40
portal_height = 60
portal_x = platform_x + platform_width - portal_width
portal_y = platform_y - portal_height
portal_color = PURPLE

clock = pygame.time.Clock()
running = True

while running:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    # def LEVELCOMPLETED():
    #   for event in pygame.event.get():
        #   if event.type == pygame.QUIT:
        #        running = False
        # text_surface = font.render("LEVEL COMPLETED!", True, BLACK)
        # text_x = (screen_width - text_surface.get_width()) // 2
        # screen.blit(text_surface, (text_x, text_y))
        # pygame.display.flip()
        # pygame.time.delay(2000) # Pause for 2 seconds
        #running = False


    # Ground collision logic
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    platform_rect = pygame.Rect(platform_x, platform_y, platform_width, platform_height)


    # Platform collision logic
    if player_rect.colliderect(platform_rect):
        # Land on platform from above
        if player_vel_y >= 0 and player_y + player_height <= platform_y + platform_height and player_y + player_height > platform_y:
            player_y = platform_y - player_height
            player_vel_y = 0
            onground = True
        # Hit head on platform from below
        elif player_vel_y < 0 and player_y < platform_y + platform_height and player_y + player_height > platform_y + platform_height:
            player_y = platform_y + platform_height
            player_vel_y = 0
            onground = False

    # Check for portal collision
    portal_rect = pygame.Rect(portal_x, portal_y, portal_width, portal_height)
    if player_rect.colliderect(portal_rect):
        pygame.display.flip()
        pygame.time.delay(500) # Pause for half a second
        running = False
    
    screen.fill(BLUE)
    # Draw border
    pygame.draw.rect(screen, GRAY, (0, 0, screen_width, screen_height), border_thickness)
    # Draw platform
    pygame.draw.rect(screen, platform_color, (platform_x, platform_y, platform_width, platform_height))
    # Draw portal
    pygame.draw.rect(screen, portal_color, (portal_x, portal_y, portal_width, portal_height))
    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
